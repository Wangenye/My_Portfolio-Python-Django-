# Generated by Django 3.1 on 2020-08-16 19:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200816_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='project_pics'),
            preserve_default=False,
        ),
    ]