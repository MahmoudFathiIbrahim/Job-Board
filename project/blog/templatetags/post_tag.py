from django import template
from blog.models import Posts, Comment

register = template.Library()
@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
    context = {
        'l_posts': Posts.objects.all()[0:5]
    }
    return context


@register.inclusion_tag('blog/latest_comments.html')
def latest_comments():
    context = {
        'l_comments': Comment.objects.filter(active=True)[0:5]
    }
    return context
