# Generated by Django 3.0.6 on 2020-05-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibloteca', '0011_auto_20200514_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='X',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asdsad', models.CharField(max_length=300)),
            ],
        ),
    ]
