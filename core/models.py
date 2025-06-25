from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    video_url = models.URLField()

    def __str__(self):
        return self.title