from django.shortcuts import render

# Create your views here.

def workout_view(request):
    return render(request, 'workout.html')


def workout_detail_view(request):
    return render(request, 'worktout-detail.html')