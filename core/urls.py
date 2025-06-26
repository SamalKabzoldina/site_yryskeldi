from rest_framework.routers import DefaultRouter
from . import views
from .views import CourseViewSet, course_list
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', views.index, name='index'),
    path('physics/', views.physics, name='physics'),
    path('api/', include(router.urls)),
    path('courses/', course_list, name='course_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

# Добавим пути от router:
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)