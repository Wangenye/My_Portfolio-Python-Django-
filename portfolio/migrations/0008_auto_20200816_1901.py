# Generated by Django 3.1 on 2020-08-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20200816_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default=None, upload_to='project_pics'),
        ),
    ]
