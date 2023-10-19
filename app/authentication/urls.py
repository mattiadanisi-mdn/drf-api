from django.urls import path, include

app_name = 'auth'
urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
