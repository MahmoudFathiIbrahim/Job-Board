from django.contrib.auth.models import User
from .models import Info
# from project.accounts.models import Profile


def my_info(request):
    info = Info.objects.first()
    context = {'info': info}
    return context


# def user_profile(request):
#     user = User.objects.get(user=request.user)
#     context = {'current_user': user}
#     return context


# def pro(request):
#     user = Profile.objects.get(user=request.user)
#     context = {'current_user': user}
#     return context


