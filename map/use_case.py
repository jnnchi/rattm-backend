
def get_locations(request):
    """
    Get all the locations of the user's transactions
    """
    lst_of_transactions = user.transactions
    locations = []
    for transaction in lst_of_transactions:
        locations.append({"location" : transaction['Location'], "Company" : transaction['Company']})
    
    return JsonResponse(locations, safe=False)