from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
  '''Моделька проекта'''
  name = models.CharField(max_length=31, unique=True) # Название
  students = models.CharField(max_length=255) # Создатели проекта
  text = models.FileField(upload_to='texts') # Описание
  short_text = models.FileField(upload_to='short_texts') # Краткое описание
  presentation = models.FileField(upload_to='presentations') # Преза
  teacher = models.ForeignKey(User, on_delete=models.CASCADE) # Руководитель

class Video(models.Model):
  '''Видео'''
  video_wishes = models.CharField(max_length=127) # Пожелания для видео
  video = models.TextField() # Видео
  project = models.ForeignKey(Project, on_delete=models.CASCADE) # Проект