from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing, name="landing"),
    path('about', views.about, name="about"),
    path('programs', views.programs, name="programs"),
    path("details/<int:pk>", views.programsDetails,name="details"),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)