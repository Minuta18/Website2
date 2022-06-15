from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.forms as aforms 
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Project
from .models import Video

class LoginForm(aforms.AuthenticationForm):
  '''Форма входа'''
  class Meta:
    model = User
    fields = ['username', 'password'] 
    
class ProjectForm(ModelForm):
  '''Форма создания нового проекта'''
  class Meta:
    model = Project
    fields = ['name', 'students']
    labels = {
      'name': 'Название проекта',
      'students': 'Участники проекта'
    }

class VideoForm(ModelForm):
  '''Форма добавления видео'''
  class Meta:
    model = Video
    fields = ['video_wishes', 'video']