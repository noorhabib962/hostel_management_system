# Generated by Django 5.1.4 on 2025-01-05 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='capcity',
            new_name='capacity',
        ),
    ]
