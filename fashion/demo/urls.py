from django.urls import path
from .views import Demo, Demo2


urlpatterns = [
    path('', Demo),
    path('common', Demo2),
    
]
