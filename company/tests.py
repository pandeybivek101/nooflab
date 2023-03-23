from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch, MagicMock
# Create your tests here.


class FetchDataViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('requests.get')
    def test_fetch_and_store_data(self, mock_get):
        # Define mocked response from the remote API
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "businessId": "1234",
                    "name": "Test Company",
                    "registrationDate": "2022-01-01",
                    "companyForm": "Ltd.",
                    "postalcode": "02100"
                }
            ]
        }
        mock_response.status_code = status.HTTP_200_OK

        # Patch requests.get to return the mocked response
        mock_get.return_value = mock_response

        # Make a GET request to the FetchDataView
        url = reverse('fetch-data')
        response = self.client.get(url)

        # Ensure the response has a status code of 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the data was fetched and stored successfully
        expected_messages = {
            "02100": "Successfully fetched and stored",
            "00140": "Successfully fetched and stored",
            "00930": "Successfully fetched and stored",
            "00710": "Successfully fetched and stored",
            "01730": "Successfully fetched and stored",
            "00500": "Successfully fetched and stored",
            "01760": "Successfully fetched and stored",
            "01690": "Successfully fetched and stored",
            "00510": "Successfully fetched and stored",
            "00180": "Successfully fetched and stored",
        }
        self.assertEqual(response.data['message'], expected_messages)