from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course

admin.site.register(User, UserAdmin)
admin.site.register(Course)