from io import BytesIO
from pathlib import Path
from PIL import Image


from django.contrib.auth.models import User
from django.core.files import File

from django.urls import reverse
from django.db import models
import datetime
from django.utils.text import slugify


# Create your models here.


def image_resize(image):
    # -----
    image_types = {
        "jpg": "JPG",
        "JPG": "JPG",
        "jpeg": "JPEG",
        "png": "PNG",
        "gif": "GIF",
        "tif": "TIFF",
        "tiff": "TIFF",
    }
    # Open the image using Pillow
    img = Image.open(image)
    # check if either the width or height is greater than the max
    if img.width > 730 or img.height > 365:
        output_size = (730, 365)
        # Create a new resized “thumbnail” version of the image with Pillow
        img.thumbnail(output_size)
        # Find the file name of the image
        img_filename = Path(image.file.name).name
        # Spilt the filename on “.” to get the file extension only
        img_suffix = Path(image.file.name).name.split(".")[-1]
        # Use the file extension to determine the file type from the image_types dictionary
        img_format = image_types[img_suffix]
        # Save the resized image into the buffer, noting the correct file type
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Wrap the buffer in File object
        file_object = File(buffer)
        # Save the new resized file as usual, which will save to S3 using django-storages
        image.save(img_filename, file_object)

    # -----


def image_upload(instance, file_name):

    date = datetime.date.today()
    image_name, extension = file_name.split('.')


    return f"blogs/{date.year}/{date.month}/{date.day}/{instance.id}-{image_name}.{extension}"


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=image_upload, default='profile/ava3.webp')
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        # return f'/blog/{self.slug}'
        return reverse('blog:post_detail', args=[self.slug])

    def save(self, commit=True, *args, **kwargs):
        self.slug = slugify(self.title)
        # if commit:
        #     image_resize(self.image)
        super(Posts, self).save(*args, **kwargs)

        # img = Image.open(self.image.path)
        # if img.width > 730 or img.height > 365:
        #     output_size = (730, 365)
        #     img = img.resize(output_size, Image.LANCZOS)
        #     quality_val = 90
        #     img.save(self.image.path, 'JPEG', quality=quality_val)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-post_date']


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Comment')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.body
