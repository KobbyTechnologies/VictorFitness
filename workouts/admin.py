from django.contrib import admin
from .models import Equipment, Exercise, ExerciseType, ProgramWorkout, WorkoutJunction, WorkoutType


class WorkoutJunctionAdmin(admin.ModelAdmin):
    list_display = ['workout', 'exercise']

# Register your models here.
admin.site.register(Equipment)
admin.site.register(Exercise)
admin.site.register(ExerciseType)
admin.site.register(ProgramWorkout)
admin.site.register(WorkoutJunction, WorkoutJunctionAdmin)
admin.site.register(WorkoutType)