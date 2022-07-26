from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.name


class ExerciseType(models.Model):
    INTENSITY_CHOICES = (
        ("Low", "Low"),
        ("Moderate", "Moderate"),
        ("Vigorous", "Vigorous"),
    )
    name = models.CharField(max_length=255)
    intensity = models.CharField(
        choices=INTENSITY_CHOICES, max_length=200, default='Moderate')

    def __str__(self):
        return str(self.name)


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.PROTECT)
    equipment = models.ForeignKey(
        Equipment, on_delete=models.PROTECT, related_name='Equipments')
    video_title = models.CharField(max_length=1000, blank=True)
    videofile = models.FileField(
        upload_to='videos/', null=True, verbose_name="")
    duration = models.IntegerField(default=10, help_text="Duration in Minutes")
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class WorkoutType(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return str(self.name)


class ProgramWorkout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.PROTECT)
    image = CloudinaryField('image', blank=True)
    price = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class WorkoutJunction(models.Model):
    workout = models.ForeignKey(
        ProgramWorkout, on_delete=models.PROTECT, related_name='workouts')
    exercise = models.ForeignKey(
        Exercise, on_delete=models.PROTECT, related_name='exercises')
