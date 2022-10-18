from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
]

if settings.DEBUG:
    from drf_spectacular.views import (SpectacularAPIView,
                                       SpectacularRedocView,
                                       SpectacularSwaggerView)
    urlpatterns += [
        path('doc_info', SpectacularAPIView.as_view(), name='schema'),
        path('docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]
