from django.urls import path
from workouts import views


urlpatterns = [
    path('workouts', views.workout_view, name='workouts'),
    path('workout-detail', views.workout_detail_view, name='workout-detail'),
]