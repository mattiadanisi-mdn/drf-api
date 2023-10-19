from django.urls import path, include
from rest_framework.routers import DefaultRouter
from animal.views import AnimalViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=AnimalViewSet,
    basename='animal'
)

urlpatterns = router.urls
