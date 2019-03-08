from django.shortcuts import render

from django.http import HttpRequest
from customer.models import Customer


# Create your views here.
def login_page(request):
    return render(request,'customer/login.html')

def main_page(request):
    return render(request,'customer/main_page.html')

def sign_up(request):
    return render(request,'customer/sign_up.html')

def createCustomer(request):
    fName = request.POST.get('customerFirstName')
    lastName = request.POST.get('customerLastName')
    Email = request.POST.get('customerEmail')
    Password = request.POST.get('customerPassword')

    query_set = list(Customer.objects.all().filter(email=Email))
    if not query_set:
        customer_obj  =  Customer(firstName=fName,lastName=lastName,email=Email,password=Password)
        customer_obj.save()
        return render(request,'customer/login.html')
    else:
        return render(request,'customer/sign_up.html')

def validateCustomer(request):
    Email = request.POST.get('customerEmail')
    Password = request.POST.get('customerPassword')

    query_set = list(Customer.objects.all().filter(email=Email,password=Password).values())
    if query_set:
        my_dict = {'first_Name':query_set[0]['firstName']}
        return render(request,'customer/main_page.html',context=my_dict)
    else:
        return render(request,'customer/login.html')

# def readCustomer(request):
#
# def updateCustomer(request):
#
# def deleteCustomer(request):
