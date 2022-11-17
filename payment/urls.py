from django.urls import path
from . import views

urlpatterns = [
    path('payment/<int:plan_id>', views.payment, name='payment'),
    path('stk_push/<str:plan_id>', views.stk_push, name='stk_push'),
]