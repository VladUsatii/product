# Generated by Django 3.0.8 on 2020-08-23 20:43

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Add_an_education_credential',
            field=models.CharField(blank=True, max_length=200, verbose_name=users.models.Profile),
        ),
    ]
