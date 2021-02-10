from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api', views.StudentReadOnlyModelViewSet, basename="student")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
