from django.shortcuts import render
from .models import Job
# Create your views here.


def job_list(request):
    job_l = Job.objects.all()
    context = {'job_list': job_l}
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    job_d = Job.objects.get(id=id)
    context = {'job': job_d}
    return render(request, 'job/job_detail.html', context)
