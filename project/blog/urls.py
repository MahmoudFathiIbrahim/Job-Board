from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.post_list, name='blogs'),
    path('add_post/', views.PostCreateView.as_view(), name='add_post'),
    path('<str:slug>', views.post_detail, name='post_detail'),
    path('<str:slug>/edit_post', views.PostUpdateView.as_view(), name='edit_post'),
    path('<str:slug>/delete_post', views.PostDeleteView.as_view(), name='delete_post'),

]


