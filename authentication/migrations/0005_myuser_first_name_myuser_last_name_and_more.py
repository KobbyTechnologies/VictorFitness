# Generated by Django 4.0.4 on 2022-11-01 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_myuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='myuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
