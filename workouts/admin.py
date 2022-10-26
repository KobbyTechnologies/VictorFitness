from django.contrib import admin
from .models import Equipment, Exercise, ProgramWorkout, WorkoutPlan


class ProgramWorkoutAdmin(admin.ModelAdmin):
    fields= [
        'name','slug','description','level', 'image', 'last_update'
    ]
    readonly_fields = ['last_update',]
    prepopulated_fields = {
        'slug': ['name', 'level']
    }

admin.site.register(ProgramWorkout, ProgramWorkoutAdmin)

# Register your models here.
admin.site.register(Equipment)
admin.site.register(Exercise)

class WorkoutPlanAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ['name']
    }

admin.site.register(WorkoutPlan, WorkoutPlanAdmin)



