from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('about', views.about, name="about"),
    path('programs', views.programs, name="programs"),
    path("details/<int:pk>", views.programsDetails,name="details"),
]