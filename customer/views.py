from django.shortcuts import render

from django.http import HttpRequest
# Create your views here.
def login_page(request):
    return render(request,'customer/login.html')

def validateCustomer(request):
def main_page(request):
    return render(request,'customer/main_page.html')
