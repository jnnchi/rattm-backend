# env_impact_history/views.py
from rest_framework import viewsets
from .models import EnvImpactHistory
from .serializers import EnvImpactHistorySerializer

class EnvImpactHistoryViewSet(viewsets.ModelViewSet):
    queryset = EnvImpactHistory.objects.all()
    serializer_class = EnvImpactHistorySerializer
    
# Assuming that all the transactions in a user is stored in a list of dictionaries
# transactions = []

def env_score_calculator(start_date: str, end_date: str) -> float:
    """
    Calculate the environmental impact score of a user
    """
    # Assuming that we are able to get the transaction history of the user from
    # start date to end date as a list, and we have figured out how to parse through the
    # the company names, so each entry is a dictionary with the company name as the key
    # and the transaction amount as the value
    lst_of_transactions = ...
    # Env_Contribution
    env_contribution = 0
    total_spending = 0
    for transaction in lst_of_transactions:
        company_env_score = ...
        transaction_amount = ...
        env_contribution += company_env_score * transaction_amount
        total_spending += transaction_amount
    
    return env_contribution / total_spending