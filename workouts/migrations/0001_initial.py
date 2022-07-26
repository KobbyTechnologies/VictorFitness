# Generated by Django 4.0.4 on 2022-07-26 04:22

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_title', models.CharField(blank=True, max_length=1000)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Equipments', to='workouts.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('intensity', models.CharField(choices=[('Low', 'Low'), ('Moderate', 'Moderate'), ('Vigorous', 'Vigorous')], default='Moderate', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Junction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='workouts.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='workouts', to='workouts.programworkout')),
            ],
        ),
        migrations.AddField(
            model_name='programworkout',
            name='workout_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workouts.workouttype'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='exercise_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workouts.exercisetype'),
        ),
    ]