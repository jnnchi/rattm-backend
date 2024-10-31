# env_impact_history/views.py
from rest_framework import viewsets
from .models import EnvImpactHistory
from .serializers import EnvImpactHistorySerializer
from entity import get_score, get_total_green_transactions, get_most_purchased_companies, get_ESG_score_of_transaction_companies
# Here we do the data structure conversion for the entity.py functions
def get_score(request):

def get_ESG_score_of_transaction_companies(request):
    
def get_total_green_transactions(request):

def get_most_purchased_companies(request):
    
    
