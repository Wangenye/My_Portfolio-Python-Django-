# Generated by Django 3.1 on 2020-08-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200816_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='profile_image',
            field=models.ImageField(upload_to='myimages'),
        ),
    ]