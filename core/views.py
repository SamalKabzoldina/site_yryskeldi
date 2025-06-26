from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from django.contrib.auth.decorators import login_required


class CourseViewSet (viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

@login_required
def course_list(request):
    courses = Course.objects.filter(users=request.user)
    return render(request, 'course_list.html', {'courses': courses})





from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def physics(request):
    return render(request, 'physics.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request,'courses.html', {'courses': courses})


