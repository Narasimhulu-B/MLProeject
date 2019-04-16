from usermodule.usermodel import Countrymodel

class CountryOperations:
    def __init__(self, **kwargs):
        self.__countrymodel_obj=Countrymodel()
       
    def get_all_countries(self):
        try:
            data=list( Countrymodel.objects.all())
            #countrylist=[]
            #for x in data:
            #    countrydict={}
            #    countrydict["Code"]=x.Code
            #    countrydict["Name"]=x.Name
            #    countrydict["Continent"]=x.Continent
            #    countrydict["Region"]=x.Region
            #    countrydict["SurfaceArea"]=x.SurfaceArea
            #    countrydict["IndepYear"]=x.IndepYear
            #    countrydict["Population"]=x.Population
            #    countrydict["LifeExpectancy"]=x.LifeExpectancy
            #    countrydict["GNP"]=x.GNP
            #    countrydict["GNPOld"]=x.GNPOld
            #    countrydict["LocalName"]=x.LocalName
            #    countrydict["GovernmentForm"]=x.GovernmentForm
            #    countrydict["HeadOfState"]=x.HeadOfState
            #    countrydict["Capital"]=x.Capital
            #    countrydict["Code2"]=x.Code2
            #    countrylist.append(countrydict)
            return data
        except Exception as ex :
            print(ex.args[0])
            return False