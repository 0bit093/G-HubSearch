from django.shortcuts import render

from django.http import HttpRequest
from customer.models import Customer
# to logout the user
from django.contrib.auth import logout

def login_page(request):
    return render(request,'customer/login.html')

def main_page(request):
    return render(request,'customer/main_page.html')

def sign_up(request):
    return render(request,'customer/sign_up.html')

# create new customer by adding to DB
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
        # saving the user in session - to use this user's info in other views
        request.session['customer_obj'] = query_set[0]
        my_dict = {'obj': query_set[0]}
        return render(request,'customer/main_page.html',context=my_dict)
    else:
        return render(request,'customer/login.html')

# displays customer info in that particular session
def showCustomerInfo(request):
    # getting the info of user from session
    c = request.session.get('customer_obj',None)
    my_dict = {'obj': c}
    return render(request,'customer/show_customer_info.html',context=my_dict)

# sign off the customer and shows successful logout
def logout_view(request):
    logout(request)
    return render(request,'customer/logout_page.html')

# show user page by populating form with current info stored in DB for updating details
def show_update_page_view(request):
    obj = request.session.get('customer_obj')
    my_dict = {'customer': obj}
    return render(request,'customer/update_page.html',context=my_dict)

# grab values from form and update the obj in DB with new values
def updateCustomer(request):
    curr_session_obj = request.session.get('customer_obj')
    old_pswd = request.POST.get('customerPassword')
    # confirms if the customer is only updating or not by comparing old pswd in DB
    if old_pswd == curr_session_obj['password']:
        # grab values from form
        pswd_update = request.POST.get('new_password')
        fname = request.POST.get('customerFirstName')
        lname = request.POST.get('customerLastName')
        Email_updated = request.POST.get('customerEmail')
        pswd_updated = request.POST.get('new_password')
        # query DB with pswd field to get customer obj and calls update func
        Customer.objects.all().filter(password=old_pswd).update(firstName=fname,lastName=lname,email=Email_updated,password=pswd_updated)
        return True
    else:
        return False

# shows login page after customer updates info to login usng new credentials
def new_login_page(request):
    # calls func -> if returns true show login page to login with new details
    # if false redirects to same page so user can enter valid info
    if updateCustomer(request):
        return render(request,'customer/new_login_page.html')
    else:
        obj = request.session.get('customer_obj')
        my_dict = {'customer': obj}
        return render(request,'customer/update_page.html',context=my_dict)

# redirect to page for customer to enter pswd to confirm deleting account
def confirm_delete_page(request):
    return render(request,'customer/confirm_delete_page.html')

# delete customer if pswd match else redirect to same page for customer to enter correct pswd
def deleteCustomer(request):
    cust_pswd = request.POST.get('customer_pswd')
    # get current customer in this session for pswd compare
    curr_session_obj = request.session.get('customer_obj')
    if cust_pswd == curr_session_obj['password']:
        # query the customer from DB get handle to it and delete object in DB using handle
        Customer.objects.all().filter(password=cust_pswd).delete()
        # redirect to Confrimation of deleting account
        return render(request,'customer/confirm_delete_account.html')
    else:
        # redirect to same page for customer to enter correct pswd
        return render(request,'customer/confirm_delete_page.html')
