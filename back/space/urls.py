from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'upload', views.UploadViewSet, basename="upload")
router.register(r'upload/generate', views.UploadTexts, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
]