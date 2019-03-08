from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request):
    my_dict = {'insert_me': "hello baby!!"}
    return render(request,'firstApp/index.html',context=my_dict)
