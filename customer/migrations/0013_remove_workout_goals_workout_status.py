# Generated by Django 4.0.4 on 2022-05-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_workout_bmi_workout_recommendations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='Goals',
        ),
        migrations.AddField(
            model_name='workout',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
