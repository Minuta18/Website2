from django.db import models
from django.contrib.auth.models import User
from .convertors import B64Converter

class Project(models.Model):
  '''Моделька проекта'''
  name = models.CharField(max_length=31)
  text = models.CharField(max_length=511) # Описание
  short_text = models.CharField(max_length=127) # Краткое описание
  presentation = models.FileField(upload_to='presentations') # Преза
  teacher = models.ForeignKey(User, on_delete=models.CASCADE) # Руководитель

class Video(models.Model):
  '''Видео'''
  video_wishes = models.CharField(max_length=127) # Пожелания для видео
  video = models.FileField(upload_to='videos') # Видео
  project = models.ForeignKey(Project, on_delete=models.CASCADE, primary_key=True) # Проект
  