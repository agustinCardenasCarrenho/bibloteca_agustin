# Generated by Django 3.0.6 on 2020-05-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibloteca', '0015_auto_20200516_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='synopsis',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
