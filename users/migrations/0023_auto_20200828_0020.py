# Generated by Django 3.0.8 on 2020-08-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200828_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Choose_banner',
            field=models.ImageField(default='default_banner.png', upload_to='banner_pics'),
        ),
    ]
