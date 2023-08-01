from django.contrib import admin
from .models import Posts, BlogCategory, Comment
# Register your models here.

admin.site.register(Posts)
admin.site.register(BlogCategory)
admin.site.register(Comment)

