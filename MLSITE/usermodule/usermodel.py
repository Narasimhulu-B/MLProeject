from django.db import models

class Countrymodel(models.Model):
    "this is User Permissions Model"
    Code=models.CharField(max_length=100,primary_key=True)
    Name=models.CharField(max_length=100)
    Continent=models.CharField(max_length=100)
    Region=models.CharField(max_length=100)
    SurfaceArea=models.FloatField()
    IndepYear=models.CharField(max_length=100)
    Population=models.IntegerField()
    LifeExpectancy=models.FloatField()
    GNP=models.FloatField()
    GNPOld=models.FloatField()
    LocalName=models.CharField(max_length=100)
    GovernmentForm=models.CharField(max_length=100)
    HeadOfState=models.CharField(max_length=100)
    Capital=models.CharField(max_length=100)
    Code2=models.IntegerField()
    class Meta:
        db_table="country"


