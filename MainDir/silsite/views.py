from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='')
def base2(request):
  return render(request, 'silsite/base2.html')

def login(request):
  '''Страница входа'''
  text = 'Sorry, but you have to log in before using site'
  form = LoginForm(data=(request.POST or None))
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
          auth.login(request, user)
          return redirect('base')
        else:
          form = LoginForm()
          text = 'Sorry, but your account is inactive.'
      else:
        form = LoginForm()
        text = 'Invalid username or password.'
    else:
      form = LoginForm()
      text = 'Invalid username or password.'
  else:
    form = LoginForm()
    text = 'Please, fill the form'
  return render(request, 'silsite/login.html', {'form': form, 'text': text})

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