from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.forms as forms 
from django.contrib.auth.models import User

# Linux = топ
class LoginForm(forms.AuthenticationForm):
  '''Форма входа'''
  class Meta:
    model = User
    fields = ['username', 'password'] 