from django.contrib import admin
from .models import Equipment, Exercise, ProgramWorkout, WorkoutPlan
from django_summernote.admin import SummernoteModelAdmin


class ProgramWorkoutAdmin(SummernoteModelAdmin):
    summernote_fields = ['description']

    fields = [
        'name', 'slug', 'description', 'level', 'image', 'last_update'
    ]
    readonly_fields = ['last_update',]
    prepopulated_fields = {
        'slug': ['name', 'level']
    }


admin.site.register(ProgramWorkout, ProgramWorkoutAdmin)

# Register your models here.
admin.site.register(Equipment)


class ExerciseAdmin(SummernoteModelAdmin):
    summernote_fields = ['description']

    fields = [
        'name', 'description',
        'type', 'equipment', 'workout', 'videofile',
        'duration',
    ]
    list_display = [
        'name', 'equipment', 'duration', 'last_update'
    ]

    list_filter = [ 'workout', 'last_update',]


admin.site.register(Exercise, ExerciseAdmin)


class WorkoutPlanAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name']
    }


admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
