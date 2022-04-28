from django.urls import path
from . import views


urlpatterns = [
    path('customer', views.Customer, name="customer"),
    path('customerProfile', views.CustomerProfile, name="customerProfile"),
    path('gallery', views.Gallery, name="gallery"),
]
