# Generated by Django 3.0.8 on 2020-08-17 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200813_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='post_pics'),
            preserve_default=False,
        ),
    ]
