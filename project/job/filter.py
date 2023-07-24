import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Job
        fields = ['title', 'description', 'job_type', 'category', 'experience']
        # exclude = ['image', 'published_at', 'salary', 'max_salary', 'slug', 'vacancy']

