# Generated by Django 4.0.4 on 2022-05-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_workout'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='Goals',
            field=models.TextField(blank=True),
        ),
    ]
