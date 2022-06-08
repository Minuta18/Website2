from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.B64Convertor, 'name')

urlpatterns = [
  path('', views.base, name='base'),
  path('login', views.login, name='login'),
  path('projects', views.projects_view, name='projects'),
  path('<str:name>', views.project_view, name='project'),
  # path('logout', views.logout, name='logout'),
]
