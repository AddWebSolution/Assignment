from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('programs/', views.programs, name="programs"),
    path('user-programs/', views.userPrograms, name="user-programs"),
]
