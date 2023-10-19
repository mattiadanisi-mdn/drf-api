from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', include('animal.urls')),
    path('users/', include('user.urls')),
    path('auth/', include('authentication.urls')),
    path('adoptions/', include('adoption.urls')),
] 
