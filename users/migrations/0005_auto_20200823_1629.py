# Generated by Django 3.0.8 on 2020-08-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='education',
            new_name='education_credential',
        ),
    ]
