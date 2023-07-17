from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def job_list(request):
    return HttpResponse('welcome job board')


def job_detail(request, job_id):
    pass
