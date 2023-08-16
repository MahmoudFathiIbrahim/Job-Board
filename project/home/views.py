from django.shortcuts import render
from job.models import Job, Category
from job.filter import JobFilter
from django.db.models import Count



# Create your views here.


def index(request):
    job_l = Job.objects.all().order_by('-published_at')
    category_l = Category.objects.annotate(number_of_categories=Count("jobs")).all().order_by('name')

    job_list = job_l[0:5]
    print(job_list)
    my_filter = JobFilter(request.GET, queryset=job_l)  # (data from get , queryset with items)
    job_l = my_filter.qs  # restore the data with filter

    context = {
        'jobs': job_l,
        'job_list': job_list,
        'my_filter': my_filter,
        'category_l': category_l,
    }
    return render(request, 'home/index.html', context)

