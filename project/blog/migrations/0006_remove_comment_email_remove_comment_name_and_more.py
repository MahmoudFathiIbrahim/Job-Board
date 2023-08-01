# Generated by Django 4.2.3 on 2023-07-26 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0005_alter_posts_options_alter_posts_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="email",),
        migrations.RemoveField(model_name="comment", name="name",),
        migrations.AddField(
            model_name="comment",
            name="commenter",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="comment",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
