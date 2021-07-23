from django.urls import path
from .views import demo, demo2, contact

app_name = 'Demo'

urlpatterns = [
    path('', demo, name='home'),
    path('common', demo2),
    path('contact', contact, name='home'),
    
]
