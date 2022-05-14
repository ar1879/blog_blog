from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    
    path('', views.home, name = 'index'),
    path('generales/', views.generales, name = 'generales'),
    path('Programacion/', views.programacion, name = 'programacion'),
    path('tutoriales/', views.tutoriales, name = 'tutoriales'),
    path('videojuegos/', views.videojuegos, name = 'videojuegos'),
    path('post/<slug:slug>/', views.detallePosts, name= "detalle_post"),
    
    
]