from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name='accounts'
urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout')
]
