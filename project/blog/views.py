from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Subquery
from django.shortcuts import render, get_object_or_404
from .models import Posts, Comment
from django.apps import apps
from .forms import CommentForm
# Create your views here.


# @login_required
def post_list(request):
    posts = Posts.objects.all()

    # Paginator
    paginator = Paginator(posts, 2)  # show 3 job per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'posts': page_obj}

    return render(request, 'blog/blog.html', context)


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



