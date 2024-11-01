# env_impact_history/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_score, get_total_green_transactions, get_most_purchased_companies

urlpatterns = [
    path('get_scr', get_score, name='get_score'),
    path('get_green_transact', get_total_green_transactions, name='get_green_transact'),
    path('get_most_purchased', get_most_purchased_companies, name='get_most_purchased'),
]