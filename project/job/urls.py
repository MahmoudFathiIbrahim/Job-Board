from django.urls import path
from . import views
from . import api

app_name = 'job'  # it`s important to make namespace in main project urls file,  namespace = name in path function

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add/', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    path('<str:slug>/edit_job', views.PostUpdateView.as_view(), name='edit_job'),
    path('<str:slug>/delete_job', views.PostDeleteView.as_view(), name='delete_job'),

    # API
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),

    # class based views
    path('api/cbv/jobs', api.JobListApi.as_view(), name='JobListApi'),
    path('api/cbv/jobs/<int:id>', api.JobDetailApi.as_view(), name='JobDetailApi'),

]
