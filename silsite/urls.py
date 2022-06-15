from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import server_error, page_not_found, permission_denied
from . import views

urlpatterns = [
  path('', views.main_page, name='main_page'),
  path('login/', views.login, name='login'),
  path('projects/project/<int:id>/', views.project_view, name='project_view'),
  path('projects/new/', views.new_project, name='new_project'),
  path('logout/', views.logout, name='logout'),
  path('error/', views.error_404, name='error'),
  path('projects/project/<int:id>/edit/', views.edit_project, name='edit_project'),
  path('projects/project/<int:id>/delete/', views.delete_project, name='delete_project'),
  path('projects/project/<int:id>/add/', views.add_video, name='add_video'),
  path('user/<str:name>/', views.user_view, name='user_view'),
  path('privacy/', views.privacy, name='privacy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)