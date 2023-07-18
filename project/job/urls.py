from django.urls import path
from . import views

app_name = 'job'  # it`s important to make namespace in main project urls file,  namespace = name in path function

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_detail, name='job_detail'),
]
