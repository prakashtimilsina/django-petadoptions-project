# Generated by Django 5.1.1 on 2024-09-26 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='decription',
            new_name='description',
        ),
    ]
