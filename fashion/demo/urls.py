from django.urls import path
from .views import Demo, Demo2

app_name = 'Demo'

urlpatterns = [
    path('', Demo, name='home'),
    path('common', Demo2),
    
]
