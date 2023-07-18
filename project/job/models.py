from django.db import models
import datetime
# Create your models here.


def image_upload(instance, file_name):
    date = datetime.date.today()
    print(date)
    image_name, extension = file_name.split('.')
    return f"jobs/{date.year}/{date.month}/{date.day}/{instance.id}-{image_name}.{extension}"


class Job(models.Model):
    job_type_choices = (('Full Time', 'Full Time'),
                        ('Part Time', 'Part Time'))
    title = models.CharField(max_length=150)
    # location
    job_type = models.CharField(max_length=30, choices=job_type_choices)
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    max_salary = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)  # 'photos/%y/%m/%d'


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

