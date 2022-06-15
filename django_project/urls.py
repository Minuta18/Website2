from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

handler404 = "silsite.views.error_404"
handler500 = "silsite.views.error_500"

urlpatterns = [
    path('', include('silsite.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
