"""
Definition of urls for MLSITE.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
from app import userurls

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),
    url(r'^get_userdata$',app.views.get_userdata,name="get_userdata"),
    url(r'^insert_userdata$',app.views.insert_userdata,name="insert_userdata"),
    url(r'^insert_user_profile$',app.views.insert_user_profile,name="insert_user_profile"),
    url(r'^getcountries$',app.views.counry_view, name='getcountries'),
    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin: 
    #username: narasimha , password: 123456789
     url(r'^admin/', admin.site.urls),
     url(r'usermodule/', include(userurls.user_urls_patterns)),
]
