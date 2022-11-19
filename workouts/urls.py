from django.urls import path
from workouts import views


urlpatterns = [
    path('workout-list', views.WorkoutListView.as_view(), name='workout-list'),
    # path( 'workouts', views.workout_view, name='workouts'),
    path('workouts/<slug:slug>/<int:pk>', views.WorkoutDetailView.as_view(), name='workout_detail'),
    # path('workout-detail', views.workout_detail_view, name='workout-detail'),
    path('workoutPlans',views.WorkoutPlansView.as_view(), name='workoutPlans'),
    path('workoutPlans/<int:pk>/<slug:slug>', views.PlanDetailView.as_view(), name='planDetails')
]