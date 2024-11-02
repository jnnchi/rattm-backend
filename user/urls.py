from django.urls import path
from .views import get_user_ip_from_frontend

urlpatterns = [
    path('get_ip/', get_user_ip_from_frontend, name='get_user_ip')
]