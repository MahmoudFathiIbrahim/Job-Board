# Generated by Django 4.2.3 on 2023-07-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0005_job_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Apply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=80)),
                ("website", models.URLField()),
                ("cv", models.FileField(upload_to="apply/")),
                ("cover_letter", models.TextField(max_length=500)),
            ],
        ),
    ]
