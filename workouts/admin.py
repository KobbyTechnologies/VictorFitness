from django.contrib import admin
from .models import Equipment, Exercise, ProgramWorkout



# Register your models here.
admin.site.register(Equipment)
admin.site.register(Exercise)
admin.site.register(ProgramWorkout)
