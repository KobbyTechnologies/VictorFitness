from unicodedata import name
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customer', views.Customer, name="customer"),
    path('customerProfile', views.CustomerProfile, name="customerProfile"),
    path('gallery', views.Gallery_Request, name="gallery"),
    path('workout',views.workout,name='workout'),
    path('report',views.my_view,name='report'),
    path('goals',views.WorkoutGoals,name='goals'),
    path('customerLibrary',views.CustomerLibrary,name='customerLibrary'),
    path('userinfo',views.userInfo,name='userinfo'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)