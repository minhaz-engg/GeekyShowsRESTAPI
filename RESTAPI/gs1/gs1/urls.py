from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:pk>/', views.student_detail),
    path('api/', views.student_list),
]
