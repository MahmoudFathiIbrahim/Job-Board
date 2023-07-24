from django.urls import path
from . import views
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
app_name = 'accounts'  # it`s important to make namespace in main project urls file,  namespace = name in path function

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]
