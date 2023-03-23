from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CompanySerializer(serializers.ModelSerializer):

    detailsUri = SerializerMethodField()

    class Meta:
        model=Company
        fields=['businessId', 'name', 'registrationDate', 'companyForm', 'detailsUri']

    
    def get_detailsUri(self, obj):
        return f"http://avoindata.prh.fi/opendata/bis/v1/{obj.businessId}"
    


