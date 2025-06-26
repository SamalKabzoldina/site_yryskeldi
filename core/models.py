from django.db import models
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    language = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    video_url = models.URLField()
    users = models.ManyToManyField('User', related_name='courses', blank=True)

    def __str__(self):
        return self.title



class User(AbstractUser):
    # Дополнительные поля при необходимости
    pass