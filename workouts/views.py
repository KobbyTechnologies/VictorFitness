from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from .models import ProgramWorkout, Exercise
from django.views.generic import ListView, DetailView

# Create your views here.


class WorkoutListView(ListView):
    template_name = 'workout.html'
    context_object_name = 'workout_list'
    queryset = ProgramWorkout.objects.order_by('-last_update').all()
    # paginate_by = 10


def workout_view(request):
    workout = ProgramWorkout.objects.all()
    context = {'workout': workout}
    return render(request, 'workout.html', context)


def workout_detail_view(request):
    return render(request, 'worktout-detail.html')
