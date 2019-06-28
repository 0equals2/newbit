from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('about/', views.about, name="about"),
    path('topic/<int:article_id>/', views.topic, name="topic"),
    path('topic/<int:article_id>/article', views.article, name="article"),
]