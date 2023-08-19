from django.contrib.auth.models import User
from django.db import models
import datetime

from django.urls import reverse
from django.utils.text import slugify
from cities_light.models import City
# Create your models here.


def image_upload(instance, file_name):
    date = datetime.date.today()
    print(date)
    image_name, extension = file_name.split('.')
    return f"jobs/{date.year}/{date.month}/{date.day}/{instance.id}-{image_name}.{extension}"


class Job(models.Model):
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    job_type_choices = (('Full Time', 'Full Time'),
                        ('Part Time', 'Part Time'))
    title = models.CharField(max_length=150)
    location = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
    job_type = models.CharField(max_length=30, choices=job_type_choices)
    description = models.TextField()
    responsibility = models.TextField(null=True, blank=True)
    qualifications = models.TextField(null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    max_salary = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', related_name='jobs', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload, default='profile/ava3.webp')  # 'photos/%y/%m/%d'

    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        # return f'/blog/{self.slug}'
        return reverse('jobs:job_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Apply(models.Model):
    name = models.CharField(max_length=50, name='first_name', verbose_name='Name')
    email = models.EmailField(max_length=80)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/%y/%m/%d')
    cover_letter = models.TextField(max_length=500)
    job_title = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='apply_job')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

