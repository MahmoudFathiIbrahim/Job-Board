from django.urls import path
from . import views

app_name = 'home'  # it`s important to make namespace in main project urls file,  namespace = name in path function

urlpatterns = [
    path('', views.index, name='index'),

]
