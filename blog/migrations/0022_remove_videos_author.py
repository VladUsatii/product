# Generated by Django 3.0.8 on 2020-08-25 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_videos_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='author',
        ),
    ]
