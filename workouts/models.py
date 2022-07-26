from tkinter import CASCADE
from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.



class Equipment(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return super(self.name)

class Exercise_Type(models.Model):
    INTENSITY_CHOICES = (
        ("Low", "Low"),
        ("Moderate", "Moderate"),
        ("Vigorous", "Vigorous"),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    intensity = models.CharField(
        choices=INTENSITY_CHOICES,max_length=200 , default='Moderate')
    video_title = models.CharField(max_length=1000, blank=True)
    videofile = models.FileField(
        upload_to='videos/', null=True, verbose_name="")


    def __str__(self):
        return str(self.name)



class Exercise(models.Model):
    name = models.CharField(max_length=200)
    exercise = models.ForeignKey(Exercise_Type, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='Equipments')
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Workout_Type(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return str(self.name)


class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    exercises = models.ManyToManyField(Exercise)
    image = CloudinaryField('image', blank=True)
    price = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Workout_Junction(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workouts')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercises')


