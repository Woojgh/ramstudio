# Generated by Django 2.0.2 on 2018-02-15 05:13

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20180214_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='images/'),
        ),
    ]