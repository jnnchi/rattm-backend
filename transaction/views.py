from django.http import JsonResponse
from utils.firebase import db
from dotenv import load_dotenv
import csv
import json
import os

# Put data in Firestore
# endpoint: /api/upload
def upload_data_to_firestore(request):
    load_dotenv()
    mock_json_path = os.getenv('MOCK_JSON_PATH')
    with open(mock_json_path, 'r') as file:
        data = json.load(file)

    try:
        for transaction in data['data']:
            transaction_id = transaction.get("transactionID")  # Get the transaction ID
            # Remove 'transactionID' from the dictionary to avoid duplication in Firestore
            transaction_data = {k: v for k, v in transaction.items() if k != "transactionID"}
            # Use transaction_id as the document ID and add the rest as the document data
            db.collection('transactions').document(str(transaction_id)).set(transaction_data)
        return JsonResponse({'message': 'Data uploaded successfully'}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Get data from Firestore
# endpoint: /api/get
def get_data_from_firestore(request):
    try:
        transactions_ref = db.collection('transactions')
        docs = transactions_ref.stream()

        transactions = []
        # a document is a row in the table (transaction obj)
        for doc in docs:
            transaction = doc.to_dict()
            transaction["rating"] = esg_rating(transaction)
            transactions.append(transaction)

        return JsonResponse(transactions, safe=False, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

# Fake function rn to give esg rating for company
def esg_rating(transaction_dict):
    print(transaction_dict)
    return len(transaction_dict["Company Name"]) // 3

# Function to convert csv to json, not needed rn
"""
def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {}
    
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
            
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            data[key] = rows

    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
"""

# convert parquet to csv: 
