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
    # if returned query set empty -> user not in DB so create the user and add to DB
    if not query_set:
        customer_obj  =  Customer(firstName=fName,lastName=lastName,email=Email,password=Password)
        customer_obj.save()
        # return control to login-page for new user to login using his/her info
        return render(request,'customer/login.html')
    else:
        return render(request,'customer/sign_up.html')

# checks if entered user credentials in DB or not
def validateCustomer(request):
    Email = request.POST.get('customerEmail')
    Password = request.POST.get('customerPassword')
    # typecasting QuerySet to list explicitly and accessing as a dictionary
    query_set = list(Customer.objects.all().filter(email=Email,password=Password).values())
    # if returned query set not empty -> user match in DB
    if query_set:
        my_dict = {'obj': query_set[0]}
        return render(request,'customer/main_page.html',context=my_dict)
    else:
        return render(request,'customer/login.html')

# def showCustomer(request):



# def updateCustomer(request):
#
# def deleteCustomer(request):
