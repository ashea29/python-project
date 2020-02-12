from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('directors/', views.DirectorList.as_view(), name='director_list'),
    path('directors/<int:pk>', views.DirectorDetail.as_view(), name='director_detail'),
    path('movies/', views.MovieList.as_view(), name="movie_list"),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name="movie_detail")
]
