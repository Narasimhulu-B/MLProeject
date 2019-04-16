from django.conf.urls import url
import app.views

user_urls_patterns=[
    url(r'^get_userdata$', app.views.get_userdata)
    ]

print(user_urls_patterns)