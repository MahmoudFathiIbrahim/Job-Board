# Generated by Django 4.2.3 on 2023-07-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_profile_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="job_title",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
