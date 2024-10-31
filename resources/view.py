import csv
from firebase_admin import credentials, firestore

csv_file_path = 'resources/ESG_data.csv'
# Missing the firestore credentials
db = firestore.client()

environment_scores = []
# First file read to get the min and max scores
with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        environment_score = float(row['environment_score'])
        environment_scores.append(environment_score)

min_score = min(environment_scores)
max_score = max(environment_scores)

# Second file read to calculate and upload the data
with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # if the score is high, 
        # then the company has a positive environmental impact
        company_name = row['name']
        environment_score = float(row['environment_score'])
        environment_grade = row['environment_grade']
        # Normalizing the score to be between 0 and 1
        normalized_score = (environment_score - min_score) / (max_score - min_score)
        data = {
            'company_name': company_name,
            'environment_grade': environment_grade,
            'environment_score': environment_score,
            'normalized_score': normalized_score
        }
        # Create or update a document in the 'companies' collection
        # Use company_name as the document ID to ensure uniqueness
        db.collection('companies').document(company_name).set(data)
        
        
        
        