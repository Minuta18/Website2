from django.urls import path
from . import views

urlpatterns = [
  path('', views.base, name='base'),
  path('login/', views.login, name='login'),
  path('projects/', views.projects_view, name='projects'),
  path('<name: str>/', views.project_view, name='project'),
  # path('logout', views.logout, name='logout'),
]
