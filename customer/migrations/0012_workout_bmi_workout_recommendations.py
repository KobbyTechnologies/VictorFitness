# Generated by Django 4.0.4 on 2022-05-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_workout_goals'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='bmi',
            field=models.IntegerField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='workout',
            name='recommendations',
            field=models.TextField(blank=True),
        ),
    ]
