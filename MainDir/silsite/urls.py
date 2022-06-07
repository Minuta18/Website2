from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.base, name='base'),
  path('login/', views.login, name='login'),
  path('projects/project/<str:name>/', views.project_view, name='project'),
  path('projects/new/', views.new_project, name='new_project')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
