from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignupForm, ProfileForm, UserForm
from .models import Profile
from blog.models import Posts, Comment
from django.core.paginator import Paginator

# Create your views here.


def signup(request):
    if request.method == 'POST':
        dataform = SignupForm(request.POST)
        if dataform.is_valid():
            dataform.save()
            username = dataform.cleaned_data['username']  # get username from the form
            password = dataform.cleaned_data['password1']  # get password from the form
            user = authenticate(username=username, password=password)  # check if this user in db
            login(request, user)
            return redirect(reverse('home:index'))
    context = {'form': SignupForm}
    return render(request, 'accounts/signup.html', context)


@login_required
def profile(request, slug=0):
    
    if slug:
        prof = Profile.objects.get(slug=slug)  # request.user: to get the logged user
    else:
        prof = Profile.objects.get(slug=request.user.profile.slug)

    user_posts = Posts.objects.filter(author=prof.user)
    paginator = Paginator(user_posts, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    comments = Comment.objects.filter(commenter=prof.user)[0:5]


    context = {
        'profile': prof,
        'posts': page_obj,
        'comments': comments,
    }
    return render(request, 'accounts/profile.html', context)


def profile_edit(request, slug):
    prof = Profile.objects.get(slug=slug)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=prof)
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            my_prof_form = profile_form.save(commit=False)
            my_prof_form.user = request.user
            my_prof_form.save()
            return redirect(reverse('accounts:profile', args=[slug]))
    context = {'profile_form': ProfileForm(instance=prof),  # to get the profile data for current user
               'user_form': UserForm(instance=request.user)}  # to get user data for current user
    return render(request, 'accounts/profile_edit.html', context)

