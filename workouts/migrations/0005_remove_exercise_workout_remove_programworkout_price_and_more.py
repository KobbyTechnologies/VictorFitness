# Generated by Django 4.0.4 on 2022-07-26 20:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_exercise_workout_alter_exercise_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.RemoveField(
            model_name='programworkout',
            name='price',
        ),
        migrations.CreateModel(
            name='WorkoutEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField(default=datetime.date.today)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('exercise', models.ManyToManyField(to='workouts.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workouts.programworkout')),
            ],
        ),
    ]
