from django.urls import path
from . import views

urlpatterns = [
    path('payment/<int:pkg_id>', views.payment, name='payment'),
]