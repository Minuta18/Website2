from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.main_page, name='main_page'),
  path('login/', views.login, name='login'),
  path('projects/project/<str:name>/', views.project_view, name='project_view'),
  path('projects/new/', views.new_project, name='new_project'),
  path('logout/', views.logout, name='logout'),
  path('error_404/', views.error_404, name='error_404'),
  path('projects/', views.projects_view, name='projects'),
  path('projects/project/<str:name>/edit/', views.edit_project, name='edit_project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
