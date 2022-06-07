from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import get_user
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.http import Http404
from .models import Project
from base64 import b64decode

@login_required(redirect_field_name='')
def base2(request):
  return render(request, 'silsite/base2.html')

def login(request):
  '''Страница входа'''
  text = ''
  form = LoginForm(data=(request.POST or None))
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active: # TODO: Зачем? #Нужно. # Ок
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
      text = 'Please, fill the form.'
  return render(request, 'silsite/login.html', {'form': form, 'text': text})

def new_project(request):
  form = ProjectForm()
  if request.method == 'POST':
    form = ProjectForm(data = request.POST)
    if form.is_valid():
      prj = form.save()
      prj.presentation = request.FILES['presentation']
      prj.save()
      print('Project created')
      return redirect('/')
    else:
      form = ProjectForm()
      print("Project don't created")
  return render(request, 'silsite/new_project.html', {'form': form})

def project_view(request, name):
  try:
    project = Project.objects.filter(name=b64decode(name))
  except Project.DoesNotExist:
    return render(request, 'silsite/error_404.html')
  return render(request, 'silsite/project.html', {'project': project})

def logout(request):
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
      return redirect('base')
  else:
    return render(request, 'silsite/logout.html', {'username': request.user.username})