# Generated by Django 2.0.2 on 2018-02-20 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20180220_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='projects.Photo'),
        ),
    ]
