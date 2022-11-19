from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('alt', views.landing, name="landing_alt"),
    path('', views.landing_alt, name="landing"),
    path('about', views.about, name="about"),
    path('programs', views.programs, name="programs"),
    path("details/<int:pk>", views.programsDetails,name="details"),
    path('personal', views.personal, name='personal'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)