# Generated by Django 2.0.2 on 2018-02-14 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180213_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photos',
            field=models.ManyToManyField(related_name='projects', to='projects.Photo'),
        ),
    ]