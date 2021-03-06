# Generated by Django 4.0.4 on 2022-05-01 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_remove_workout_goals_workout_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='gender',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='customer.userinfo'),
        ),
        migrations.AddField(
            model_name='workout',
            name='hip',
            field=models.IntegerField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='workout',
            name='waist',
            field=models.IntegerField(blank=True, default=0.0),
        ),
    ]
