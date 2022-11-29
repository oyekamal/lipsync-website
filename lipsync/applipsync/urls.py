from rest_framework import routers
from .views import FileViewSet, VideoFrameViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register('file', FileViewSet)
router.register('video_frame', VideoFrameViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]