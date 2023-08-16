import django_filters
from .models import Posts


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Posts
        fields = ['title', 'content', 'category']
        # exclude = ['image', 'published_at', 'salary', 'max_salary', 'slug', 'vacancy']
