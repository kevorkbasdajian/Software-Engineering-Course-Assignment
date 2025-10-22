from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('update_movie/', views.update_movie, name='update_movie'),
    path('delete_movie/', views.delete_movie, name='delete_movie'),
    path('display_movies/', views.display_movies, name='display_movies'),
    path('Display_movie/', views.display_movie, name='display_movie'),
]
