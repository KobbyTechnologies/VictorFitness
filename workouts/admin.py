from django.contrib import admin
from .models import Equipment, Exercise, ProgramWorkout


class ProgramWorkoutAdmin(admin.ModelAdmin):
    fields= [
        'name','slug','description','level', 'image', 'last_update'
    ]
    readonly_fields = ['last_update',]
    prepopulated_fields = {
        'slug': ['name', 'level']
    }


# Register your models here.
admin.site.register(Equipment)
admin.site.register(Exercise)
admin.site.register(ProgramWorkout, ProgramWorkoutAdmin)
