# Generated by Django 5.0.7 on 2024-08-28 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_library_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages_count',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 10, 45)),
        ),
    ]
