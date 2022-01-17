from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')), 
]

if settings.DEBUG:
    urlpatterns += [path('__silk/', include('silk.urls', namespace='silk'))]