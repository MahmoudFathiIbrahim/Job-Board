from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

# Create your views here.


def job_list(request):
    job_l = Job.objects.all()
    paginator = Paginator(job_l, 1)  # show 1 job per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'job_list': page_obj}
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    job_d = Job.objects.get(id=id)
    min_salary = job_d.salary*12/1000
    max_salary = job_d.max_salary*12/1000
    context = {'job': job_d, 'min_salary': min_salary, 'max_salary': max_salary}
    return render(request, 'job/job_detail.html', context)
