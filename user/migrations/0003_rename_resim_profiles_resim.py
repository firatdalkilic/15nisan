# Generated by Django 4.1.1 on 2023-06-03 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profiles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='Resim',
            new_name='resim',
        ),
    ]
