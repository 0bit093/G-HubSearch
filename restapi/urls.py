from django.urls import path, include

from restapi import views

urlpatterns = [
    path('find/',views.find_user,name='find_user')
]
