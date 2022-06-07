from django.urls import path
from . import views

urlpatterns = [
  path('', views.base2, name='base'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
]
