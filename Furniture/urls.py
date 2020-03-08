# from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('myadmin/', include('adminapp.urls', namespace='myadmin')),
    # path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)