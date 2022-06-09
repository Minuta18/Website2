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
          return redirect('main_page')
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

@login_required(redirect_field_name='')
def new_project(request):
  '''Новый проект'''
  form = ProjectForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      prj = Project()
      prj.name = form.cleaned_data['name']
      if request.FILES.get('short_text') != None and request.FILES.get('text') != None and request.FILES.get('presentation') != None:
        prj.short_text = request.FILES['short_text']
        prj.text = request.FILES['text']
        prj.presentation = request.FILES['presentation']
      else:
        form = ProjectForm(instance=prj)
        return render(request, 'silsite/new_project.html', {'form': form})
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
  return render(request, 'silsite/project_view.html', {'project': project, 'username': request.user.username})

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

@login_required(redirect_field_name='')
def edit_project(request, name):
  prj = Project.objects.filter(name=name)[0]
  if request.user.username != prj.teacher.username:
    return redirect('project_view')
  form = ProjectForm()
  if request.method == 'POST':
    form = ProjectForm(request.POST, instance=prj)
    if form.is_valid():
      prj.name = form.cleaned_data['name']
      if request.FILES.get('short_text') != None and request.FILES.get('text') != None and request.FILES.get('presentation') != None:
        prj.short_text = request.FILES['short_text']
        prj.text = request.FILES['text']
        prj.presentation = request.FILES['presentation']
      else:
        form = ProjectForm(instance=prj)
        return render(request, 'silsite/edit_project.html', {'form': form})
      prj.teacher = request.user
      prj.save()
      return redirect('projects')
  else:
    form = ProjectForm(instance=prj)
  return render(request, 'silsite/edit_project.html', {'presentation': prj.presentation, 'form': form})