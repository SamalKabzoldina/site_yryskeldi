from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('physics/', views.physics, name='physics'),  # <- ОБЯЗАТЕЛЬНО этот маршрут
]