
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('app/', include('cashbank.urls')),
]
