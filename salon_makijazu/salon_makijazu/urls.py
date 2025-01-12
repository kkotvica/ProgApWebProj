from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rezerwacje.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rezerwacje.api_urls')),
    path('', auth_views.LoginView.as_view(template_name='rezerwacje/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('', include('rezerwacje.urls')),
]