from django.urls import path
from . import views


urlpatterns = [
    path('customer', views.Customer, name="customer"),
    path('customerProfile', views.CustomerProfile, name="customerProfile"),
    path('gallery', views.Gallery_Request, name="gallery"),
    path('hover', views.Hover, name="hover"),
]
