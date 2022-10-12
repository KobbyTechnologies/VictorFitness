from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:pkg_id>', views.payment, name='payment'),
]