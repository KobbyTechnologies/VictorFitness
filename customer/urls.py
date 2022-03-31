from django.urls import path

from . import views

urlpatterns = [
    path('customer', views.Customer, name="customer"),
]
