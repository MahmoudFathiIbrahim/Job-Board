# Generated by Django 4.2.3 on 2023-07-25 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="author",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="blog.blogcategory"
            ),
        ),
    ]