from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE,
                             null=True, blank=True, default='')
    phone_number = PhoneNumberField(blank=True, region='EG')
    image = models.ImageField(upload_to='profile/%y/%m/%d', default='profile/ava3.webp')
    job_title = models.CharField(max_length=50, null=True, blank=True, default='Job Title')

    def __str__(self):
        return str(self.user)


# https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
# initialize the function as receiver
@receiver(post_save, sender=User)  # post_save = after save in db send signal
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
