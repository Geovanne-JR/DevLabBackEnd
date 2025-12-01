from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # envia tudo pro centro
    path('api/', include('centro.urls')),
]