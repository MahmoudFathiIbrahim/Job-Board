from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number = PhoneNumberField(region='EG')
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.place

