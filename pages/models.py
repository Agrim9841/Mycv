from django.db import models
from datetime import datetime


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    technology = models.CharField(max_length=150, blank=True, default='')
    image_1 = models.ImageField(upload_to="project_image/%Y%m%d", default="", null=True, blank=True)
    image_2 = models.ImageField(upload_to="project_image/%Y%m%d", default="", null=True, blank=True)
    image_3 = models.ImageField(upload_to="project_image/%Y%m%d", default="", null=True, blank=True)
    description = models.TextField(max_length=1000, default='', blank=True)
    github_link = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    file = models.FileField(upload_to='resume/',blank=True)



class Contact(models.Model):
    name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(default="", blank=False)
    message = models.TextField(blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.name

