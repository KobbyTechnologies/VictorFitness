from django.urls import path, re_path
from workouts import views


urlpatterns = [
    path('workout-list', views.WorkoutListView.as_view(), name='workout-list'),
    # path( 'workouts', views.workout_view, name='workouts'),
    path('workouts/<slug:slug>/<int:pk>', views.WorkoutDetailView.as_view(), name='workout_detail'),
    # path('workout-detail', views.workout_detail_view, name='workout-detail'),
]