# Generated by Django 3.0.8 on 2020-08-24 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_add_current_employer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Add_current_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
