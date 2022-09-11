from django.urls import path
from . import views

urlpatterns = [
    path('articles', views.ArticleView.as_view(), name='articles'),
    # path('articles', views.article_view, name='articles'),
    path('articles/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail')
]