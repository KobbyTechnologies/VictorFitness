from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from .models import ProgramWorkout, Exercise
from post.models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


class WorkoutListView(ListView):
    template_name = 'workout.html'
    context_object_name = 'workout_list'
    queryset = ProgramWorkout.objects.order_by('-last_update').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    # paginate_by = 10


class WorkoutDetailView(DetailView):
    template_name = 'worktout-detail.html'
    model = ProgramWorkout

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        programworkout_pk = self.kwargs.get('pk', None)
        context['exercises'] = Exercise.objects.filter(workout=programworkout_pk).all()
        context['related_articles'] = Post.objects.filter(workout=programworkout_pk).all()[:4]
        return context

