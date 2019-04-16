"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from usermodule import userprofile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import RP_USER_PROFILE
from usermodule.userprofile import CountryOperations

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def insert_user_profile(request):
    try:
       if request.method=="POST" :
            user_name= request.POST["username"]
            password= request.POST["password"]
            email= request.POST["email"]
            gender= request.POST["gender"]
            status=insert_user_data(user_name,password,email,gender)
            if status:
                return render(request,'usertemplates/userdetails.html',{"status":"Inserted Sucessfully"})
            else:
                return render(request,'usertemplates/userdetails.html',{"status":"Not Inserted"})
       else:
            return render(request,'usertemplates/userdetails.html')

    except Exception as ex :
        print(ex.args[0])
        return render(request,'usertemplates/userdetails.html',{"status":"Not Inserted"})

def counry_view(request):
    try:
        countrylist=CountryOperations().get_all_countries()
        cols= ['Code',
                'Name',
                'Continent',
                'Region',
                'IndepYear',
                'Population',
                'LifeExp',
                'GNP',
                'GNPOld',
                'LocalName',
                'GovtForm',
                'HeadOfState',
                'Capital',
               ]
        if request.method=="POST":

            response_data= render(request,'usertemplates/countrylist.html',{"countrylist":countrylist, "cols":cols})
            response_data.set_cookie("name","Narasimha")
            response_data.set_cookie("gender","M")
            return response_data
        else:

            response_data= render(request,'usertemplates/countrylist.html',{"countrylist":countrylist, "cols":cols})
            response_data.set_cookie("name","Narasimha")
            response_data.set_cookie("gender","M")
            return response_data
    except Exception as ex :
        print(ex.args[0])
        return render(request,'usertemplates/countrylist.html',{"countrylist":[], "cols":cols})


#from django.http import HttpResponse
#from django.template import loader

#from .models import Question


#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

@api_view(["GET"])
def get_userdata(request):
    try:
        data=getuserdata()
        myname=request.COOKIES["name"]
        return Response({"data":data})
    except Exception as ex :
        return Response ({"Error":ex.args[0]})

@api_view(["POST"])
def insert_userdata(request):
    try:
        status=insert_user_data()
        if status:
            data="Saved Successfully"
        else:
            data="Not Saved "

        return Response({"data":data})    
    except Exception as ex :
        return Response ({"Error":ex.args[0]})

def getuserdata():
    try:
        user_data=list( RP_USER_PROFILE.objects.all())
        users_list=[]
        for x in user_data:
           user_dict={}
           user_dict["id"]=x.id
           user_dict["user_name"]=x.user_name
           user_dict["uesr_password"]=x.uesr_password
           user_dict["email"]=x.email
           user_dict["gender"]=x.gender
           users_list.append(user_dict)
        return users_list
    except Exception as ex :
        print(ex.args[0])

def insert_user_data(uname,upassword,email,gender):
    try:
        u=RP_USER_PROFILE(user_name=uname,uesr_password=upassword,email=email,gender=gender)
        u.save()
        #f=RP_USER_PROFILE(user_name="shanthi",uesr_password="123456",email="shanthi.s@gmail.com",gender="Female")
        #f.save()
        return True
    except Exception as ex:
        print(ex.args[0])
        return False