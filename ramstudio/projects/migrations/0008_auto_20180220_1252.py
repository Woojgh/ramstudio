# Generated by Django 2.0.2 on 2018-02-20 12:52

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20180220_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='covers/'),
        ),
    ]