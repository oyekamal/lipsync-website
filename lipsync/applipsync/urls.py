from rest_framework import routers
from .views import FileViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register('file', FileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]