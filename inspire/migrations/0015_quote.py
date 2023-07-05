# Generated by Django 3.2.5 on 2023-06-20 03:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspire', '0014_usermessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, null=True)),
                ('created', models.DateTimeField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=list, size=None)),
                ('quote', models.TextField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
