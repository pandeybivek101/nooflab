from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer
# Create your tests here.


class GetDataViewTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()

        # Create test companies with different postal codes
        self.company1 = Company.objects.create(
            businessId='55353-11', name='Test1', registrationDate='2022-04-01', companyForm='PY', postalcode='00011'
        )
        self.company2 = Company.objects.create(
            businessId='4522-1', name='Test3', registrationDate='2021-02-01', companyForm='OX', postalcode='003331'
        )
        self.company3 = Company.objects.create(
            businessId='8880-1', name='Test3', registrationDate='2025-2-01', companyForm='LTD', postalcode='00011'
        )


    def test_get_data_view(self):
        # Test retrieving data for a valid postal code
        response = self.client.get('/postal_codes/00011/companies')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Expected 3 companies with postal code 00100
        
        # Test retrieving data for an invalid postal code
        response = self.client.get('/postal_codes/6666666/companies')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0) # Expected no companies with postal code 99999