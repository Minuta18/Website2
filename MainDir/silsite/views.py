from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import get_user
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.http import Http404
from .models import Project
from base64 import b64decode, b64encode

@login_required(redirect_field_name='')
def main_page(request):
  return render(request, 'silsite/main_page.html')

def login(request):
  '''Страница входа'''
  text = 'Sorry, but you have to login before using site.'
  form = LoginForm(data=(request.POST or None))
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
          auth.login(request, user)
          return redirect('/')
        else:
          form = LoginForm()
          text = 'Sorry, but your account is inactive.'
      else:
        form = LoginForm()
        text = 'Invalid username or password.'
    else:
      form = LoginForm()
      text = 'Invalid username or password.'
  return render(request, 'silsite/login.html', {'form': form, 'text': text})

def new_project(request):
  '''Новый проект'''
  form = ProjectForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      prj = Project()
      prj.name = form.cleaned_data['name']
      prj.short_text = form.cleaned_data['short_text']
      prj.text = form.cleaned_data['text']
      prj.presentation = request.FILES['presentation']
      prj.teacher = request.user
      prj.save()
      return redirect('projects')
    else:
      form = ProjectForm()
  return render(request, 'silsite/new_project.html', {'form': form})

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'silsite/projects.html', {'projects': projects})

def project_view(request, name):
  '''Просмотр проекта'''
  try:
    project = Project.objects.filter(name = name)[0]
  except Project.DoesNotExist:
    return render(request, 'silsite/error_404.html')
  return render(request, 'silsite/project_view.html', {'project': project})

@login_required(redirect_field_name='')
def logout(request):
  '''Выход'''
  if (request.method == 'POST'): 
    val = ''
    try:
      val = request.POST.get('Yes')
    except:
      val = 'No'
    if (val == 'Yes'):
      auth.logout(request)
      return redirect('login')
    else:
      return redirect('main_page')
  else:
    return render(request, 'silsite/logout.html', {'username': request.user.username})

def error_404(request):
  return render(request, 'silsite/error_404')