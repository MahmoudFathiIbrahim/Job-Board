from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Subquery
from django.shortcuts import render, get_object_or_404
from .models import Posts, Comment, BlogCategory
from django.apps import apps
from .forms import CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .filter import PostFilter

from django.urls import reverse_lazy



# Create your views here.


# @login_required
def post_list(request):
    posts = Posts.objects.all()

    comments = Comment.objects.filter(active=True)
    # for comment, post in comments, posts:
    #     if comment.post == post:
    #
    category = BlogCategory.objects.all()

    my_filter = PostFilter(request.GET, queryset=posts)

    posts = my_filter.qs

    # Paginator
    paginator = Paginator(posts, 2)  # show 3 job per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'posts': page_obj,
               'filter': my_filter,
               'category': category,
               'comments': comments,
               }

    return render(request, 'blog/blog.html', context)

@login_required
def post_detail(request, slug):

    post = get_object_or_404(Posts, slug=slug)
    # post = Posts.objects.get(slug=slug)
    next_post = Posts.objects.filter(id__gt=Subquery(Posts.objects.filter(slug=slug).values('id'))).order_by('category', 'id').first()
    prev_post = Posts.objects.filter(id__lt=Subquery(Posts.objects.filter(slug=slug).values('id'))).order_by('-category', '-id').first()
    Profile = apps.get_model('accounts', 'Profile')
    prof = Profile.objects.get(user=post.author)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        print('method is post'*10)
        dataform = CommentForm(request.POST)
        if dataform.is_valid():
            print('data is valid'*10)
            save_form = dataform.save(commit=False)
            save_form.post = post
            save_form.commenter = request.user
            save_form.save()

    context = {'post': post,
               'next_post': next_post,
               'prev_post': prev_post,
               'prof': prof,
               'comments': comments,
               'form': CommentForm(instance=request.user)
               }
    return render(request, 'blog/single-blog.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content', 'category', 'image']
    template_name = 'blog/add_post.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Posts
    fields = ['title', 'content', 'category', 'image']
    template_name = 'blog/edit_post.html'
    # form_class = PostCreateView
    # success_url = reverse_lazy('blog:edit_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'blog/posts_confirm_delete.html'
    success_url = '/blog'
