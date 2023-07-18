from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm


# Create your views here.


def job_list(request):
    job_l = Job.objects.all()
    paginator = Paginator(job_l, 1)  # show 1 job per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'job_list': page_obj}
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_d = Job.objects.get(slug=slug)
    min_salary = job_d.salary*12/1000
    max_salary = job_d.max_salary*12/1000

    # apply form
    if request.method == 'POST':
        dataform = ApplyForm(request.POST, request.FILES)  # request.FILES = to get files from the form like pdf files
        if dataform.is_valid():
            save = dataform.save(commit=False)
            save.job_title = job_d
            save.save()

    context = {'job': job_d, 'min_salary': min_salary, 'max_salary': max_salary,
               'form': ApplyForm}
    return render(request, 'job/job_detail.html', context)
