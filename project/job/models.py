from django.db import models
# Create your models here.




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
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

