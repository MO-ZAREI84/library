# Generated by Django 5.0.7 on 2024-08-24 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Personal',
            new_name='Person',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
