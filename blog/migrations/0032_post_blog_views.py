# Generated by Django 3.0.8 on 2020-08-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200828_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
    ]