from django.db import models

# Create your models here.
class Company(models.Model):
    """
    businessId, name, registrationDate, companyForm are enough field to store information
    detailsUri can be easily generated from the businessId
    
    """
    businessId = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    registrationDate = models.DateField()
    companyForm = models.CharField(max_length=10)
    postalcode = models.CharField(max_length=20)

    def __str__(self):
        return self.name
