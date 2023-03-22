from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

# Create your views here.
class FetchDataView(APIView):
    
    def get(self, request):

        postCodes = ["02100", "00140", "00930", "00710", "01730", "00500", "01760", "01690", "00510", "00180", "sjshshsh"]

        #looping through each postal address of Vantaa, Espoo and Helsinki
        for item in postCodes:
            try:

                """
                parameter to be pass along with the get requests as per the documentation
                http://avoindata.prh.fi/bis/v1 two main parameters required for our case
                maxResults to fetch maximum numbers of results and streetAddressPostCode to pass post code
                """

                parameters = {'maxResults': 20, 'streetAddressPostCode': item}
                res = requests.get('http://avoindata.prh.fi/bis/v1', params=parameters)
                print (res.text)

            except:
                print(f"failed to fetch data from {item} postal address")
        return Response({'name': 'bivek'})
        