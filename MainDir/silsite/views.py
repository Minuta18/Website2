from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Project
from base64 import decode


@login_required(redirect_field_name='')
def base(request):
  return render(request, 'silsite/base.html')


def login(request):
    """Страница входа"""
    text = ''
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
          text = 'Please, fill the form.'
    return render(request, 'silsite/login.html', {'form': form, 'text': text})


def projects_view(request):
    projects = Project.objects.filter()
    return render(request, 'silsite/projects.html', {'projects': projects})


def project_view(request, name):
    projects = Project.objects.filter()
    return render(request, 'silsite/project.html', {'name': name, 'projects': projects})
