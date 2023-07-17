# Generated by Django 4.2.3 on 2023-07-17 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=150)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("Full Time", "Full Time"),
                            ("Part Time", "Part Time"),
                        ],
                        max_length=30,
                    ),
                ),
                ("description", models.TextField(max_length=500)),
                ("published_at", models.DateTimeField(auto_now=True)),
                ("vacancy", models.IntegerField(default=1)),
                (
                    "salary",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                ("experience", models.IntegerField(default=1)),
            ],
        ),
    ]
