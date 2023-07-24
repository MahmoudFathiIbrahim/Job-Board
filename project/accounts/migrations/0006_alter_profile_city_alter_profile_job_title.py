# Generated by Django 4.2.3 on 2023-07-23 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="city",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_city",
                to="accounts.city",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="job_title",
            field=models.CharField(
                blank=True, default="Job Title", max_length=50, null=True
            ),
        ),
    ]
