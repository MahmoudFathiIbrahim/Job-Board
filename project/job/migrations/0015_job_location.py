# Generated by Django 4.2.3 on 2023-08-19 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('job', '0014_job_benefits'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cities_light.city'),
        ),
    ]
