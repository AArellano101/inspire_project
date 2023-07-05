# Generated by Django 3.2.5 on 2023-06-23 01:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspire', '0019_auto_20230622_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noti', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='inspireuser',
            name='notifications',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, default=list, size=None),
        ),
    ]
