from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('space/', include('space.urls')),

    path('api/',include('rest_framework.urls')),
    
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
