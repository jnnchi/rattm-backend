from django.test import TestCase, Client
from unittest.mock import patch, MagicMock
from django.http import JsonResponse
import os
import json

# Create your tests here.
class ESGTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.upload_url = '/esg/upload'
        self.get_url = '/esg/get'
        
    @patch('utils.firebase.db.collection')
    def test_get_data_from_firestore(self, mock_collection):
        # Mock Firestore db collection stream
        mock_doc = MagicMock() # Mock document
        mock_doc.to_dict.side_effect = [
            {"name": "CompanyA", "score": 85},
            {"name": "CompanyB", "score": 90}
        ]
        mock_collection.return_value.stream.return_value = [mock_doc, mock_doc]

        # Call the view
        response = self.client.get(reverse("get_data"))
        
        # Validate results
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {"name": "CompanyA", "score": 85},
            {"name": "CompanyB", "score": 90}
        ])

    @patch('utils.firebase.db.collection')
    def test_get_individual_company_score(self, mock_collection):
        # Mock Firestore query for company score
        mock_doc = MagicMock()
        mock_doc.to_dict.return_value = {"name": "CompanyA", "score": 85}
        mock_collection.return_value.where.return_value.limit.return_value.stream.return_value = [mock_doc]

        # Call the function directly (assuming it’s not a view)
        response = get_individual_company_score("CompanyA")
        
        # Validate results
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"name": "CompanyA", "score": 85})
