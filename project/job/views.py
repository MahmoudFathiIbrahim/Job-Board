from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from .filter import JobFilter

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def job_list(request):
    job_l = Job.objects.all()

    # Filters
    my_filter = JobFilter(request.GET, queryset=job_l)  # (data from get , queryset with items)
    job_l = my_filter.qs  # restore the data with filter

    # Paginator
    paginator = Paginator(job_l, 3)  # show 3 job per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'job_list': page_obj, 'my_filter': my_filter, 'jobs': job_l}
    return render(request, 'job/job_list.html', context)


@login_required
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
               'form': ApplyForm(instance=request.user)}
    return render(request, 'job/job_detail.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        dataform = JobForm(request.POST, request.FILES)  # request.FILES = to get files from the form like pdf files
        if dataform.is_valid():
            save = dataform.save(commit=False)
            save.owner = request.user
            save.save()
            return redirect(reverse('jobs:job_list'))

    context = {'form': JobForm}
    return render(request, 'job/add_job.html', context)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job/edit_job.html'

    # form_class = PostCreateView
    # success_url = reverse_lazy('blog:edit_post')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'job/job_confirm_delete.html'
    success_url = '/jobs'


