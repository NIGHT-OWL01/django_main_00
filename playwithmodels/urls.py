from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name='playwithmodels'
urlpatterns = [
    path('', views.Home.as_view(),name='Home'),
    path('temp', TemplateView.as_view(template_name='playwithmodels/temp.html'),name='temp'),
    path('ListSong', views.SongList.as_view(),name='ListSong'),
    path('CreateSong', views.CreateSong.as_view(),name='CreateSong'),
    path('<int:pk>/UpdateSong', views.UpdateSong.as_view(),name='UpdateSong'),
    path('<int:pk>/DeleteSong', views.DeleteSong.as_view(),name='DeleteSong'),
]
