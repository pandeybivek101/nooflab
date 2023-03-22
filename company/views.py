from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

# Create your views here.
class FetchDataView(APIView):

    def store(self):
        pass
    
    def get(self, request):

        postCodes = ["02100", "00140", "00930", "00710", "01730", "00500", "01760", "01690", "00510", "00180"]

        #looping through each postal address of Vantaa, Espoo and Helsinki
        for item in postCodes:
            try:

                """
                parameter to be pass along with the get request as per the documentation of PRH.
                endpoints http://avoindata.prh.fi/bis/v1 takes two parameters for our required scenario
                maxResults to limit results and streetAddressPostCode to pass post code
                """

                parameters = {'maxResults': 20, 'streetAddressPostCode': item}
                res = requests.get('http://avoindata.prh.fi/bis/v1', params=parameters)
                print (res.txt)

            except:
                print(f"failed to fetch data from {item} postal address")

        return Response({'name': 'bivek'})
        