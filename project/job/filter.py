import django_filters
from django import forms

from .models import Job, Category


class JobFilter(django_filters.FilterSet):


    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), empty_label='Category')

    class Meta:

        model = Job
        fields = ['title', 'description', 'job_type', 'category', 'experience', 'location']
        # exclude = ['image', 'published_at', 'salary', 'max_salary', 'slug', 'vacancy']



