from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
  """Моделька проекта"""
  name = models.CharField(max_length=90)  # Название
  text = models.CharField(max_length=127)  # Описание
  short_text = models.CharField(max_length=511)  # Краткое описание
  presentation = models.FileField(upload_to='./../presentations/')  # Презентация
  teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # Руководитель


class Video(models.Model):
  """Видео"""
  video_wishes = models.CharField(max_length=127)  # Пожелания для видео
  video = models.FileField(upload_to='./../videos/')  # Видео
  project = models.ForeignKey(Project, on_delete=models.CASCADE, primary_key=True)  # Проект
