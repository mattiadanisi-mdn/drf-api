from rest_framework.routers import DefaultRouter
from django.urls import path, include

from adoption.views import AdoptionViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=AdoptionViewSet,
    basename='adoptions'
)


urlpatterns = [
    path('', include(router.urls))
]

