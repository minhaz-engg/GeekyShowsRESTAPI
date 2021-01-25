from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',views.StudentList.as_view()),
    # path('api/',views.StudentCreate.as_view()),
    path('api/<int:pk>/',views.StudentRetrive.as_view()),
    # path('api/<int:pk>/',views.StudentRetriveUpdateDestroy.as_view()),
]
