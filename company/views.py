import requests
from .models import Company
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.
class FetchDataView(APIView):


    """
    This function is mainly responsible for storing the non existing data into the database
    """
    def store_fetched_data(self, data, postCode):

        #looping through the json data
        for item in data['results']:

            """
            get_or_create stores the object in database if and only if the record is not present in database else it will skip
            """
            # print(item['registrationDate'])
            Company.objects.get_or_create(
                businessId=item['businessId'], 
                name=item['businessId'], 
                registrationDate=item['registrationDate'], 
                companyForm=item['companyForm'], 
                postalcode=postCode
            )

        return

        


    """
    This function is mainly responsible for fetching the data from the remote source and the above
    function store_fetched_data() is called to store the data into database
    """
    def fetch_remote_data(self, postCode, messages):
        
        try:

            """
            parameter to be pass along with the get request as per the documentation of PRH.
            endpoints http://avoindata.prh.fi/bis/v1 takes two parameters for our required scenario
            maxResults to limit results and streetAddressPostCode to pass post code
            """

            parameters = {'maxResults': 20, 'streetAddressPostCode': postCode}
            res = requests.get('http://avoindata.prh.fi/bis/v1', params=parameters)
            

            #storing the fetched data into Database
            self.store_fetched_data(res.json(), postCode)
            messages[postCode] = "Successfully fetched and stored"

        except:
            messages[postCode] = "Something went wrong while fetching and storing"


        return messages




    def get(self, request):

        postCodes = ["02100", "00140", "00930", "00710", "01730", "00500", "01760", "01690", "00510", "00180"]
        messages = dict()
        #looping through each postal address of Vantaa, Espoo and Helsinki

        for pCode in postCodes:

            #fetching and storing the data based on the postcode
            fetchStore = self.fetch_remote_data(pCode, messages)

        return Response({'message': fetchStore}, status=status.HTTP_200_OK)
        