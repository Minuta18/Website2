from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.forms as aforms 
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Project
from .models import Video
from django import forms


class LoginForm(aforms.AuthenticationForm):
  '''Форма входа'''
  class Meta:
    model = User
    fields = ['username', 'password']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['password'].widget.attrs.update({'class': 'form-control'})


class ProjectForm(ModelForm):
  '''Форма создания нового проекта'''
  class Meta:
    model = Project
    fields = ['name']


class VideoForm(ModelForm):
  '''Форма добавления видео'''
  class Meta:
    model = Video
    fields = ['video_wishes', 'video']