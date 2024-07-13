from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.general.urls')),
    path('users/', include('apps.users.urls')),
    path('agreements_create/', include('apps.agreements.urls')),
]
