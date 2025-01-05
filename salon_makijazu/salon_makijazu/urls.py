from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rezerwacje.urls')),  # Rejestracja URL-i aplikacji rezerwacje
]