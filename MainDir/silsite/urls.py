from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('???/', views.base2, name='base'),
  path('login/', views.login, name='login'),
  path('project/<str:name>/', views.project_view, name='project'),
  path('new/', views.new_project, name='new_project'),
  path('', views.projects_view, name='projects'),
  path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
