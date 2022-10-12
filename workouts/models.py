from xml.parsers.expat import model
from django.db import models
from cloudinary.models import CloudinaryField
from customer.models import SubscriptionPlan


# Create your models here.

EXERCISE_TYPE = [
    ('Endurance', 'Endurance'),
    ('Strength', 'Strength'),
    ('Balance', 'Balance'),
    ('Flexibility', 'Flexibility')

]

WORKOUT_LEVEL = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced')
]

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProgramWorkout(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    level = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, default=1)
    image = CloudinaryField('image', blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Workout'

    def __str__(self):
        return str(self.name)


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(choices=EXERCISE_TYPE, max_length=200,  default='Balance')
    equipment = models.ForeignKey(
        Equipment, related_name='Equipments', blank=True, on_delete=models.PROTECT)
    workout = models.ForeignKey(ProgramWorkout, on_delete=models.CASCADE,related_name='Exercises')
    videofile = models.FileField(
        upload_to='videos/', blank=True, verbose_name="")
    duration = models.IntegerField(default=10, help_text="Duration in Minutes")
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
