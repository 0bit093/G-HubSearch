from django.shortcuts import render

from django.http import HttpRequest
from customer.models import Customer
import requests

def find_user(request):
    # fetch github user info from github API
    search_user_name = request.POST.get('user_to_find')
    customer_in_session = request.session.get('customer_obj')
    api_root_url = "https://api.github.com/users/"
    query_url = api_root_url + search_user_name # send a request to github api endpoint
    response = requests.get(query_url) # collect response from the endpoint
    result = response.json() # JSON data
    # fetch 'githubUserName + activity' from Customer table in DB using field 'firstName'
    cust_Dao_QS= list(Customer.objects.all().filter(firstName=customer_in_session['firstName']).values())
    if cust_Dao_QS:                                                  # query matched
        cust_obj = cust_Dao_QS[0]                                    # take first dict 
        if cust_obj['githubUserName'] and cust_obj['activity']:      # check if user already queried atleast once i.e if these 2 fields is not null
            if cust_obj['githubUserName']==search_user_name:         # check if user queried for the same username now and previous
                Customer.objects.all().filter(firstName=customer_in_session['firstName']).update(activity=result['updated_at']) # update only acticity field
            else:
                Customer.objects.all().filter(firstName=customer_in_session['firstName']).update(githubUserName=search_user_name,activity=result['updated_at'])
        else:
            Customer.objects.all().filter(firstName=customer_in_session['firstName']).update(githubUserName=search_user_name,activity=result['updated_at'])
    # add github user info JSON obj to dict and send 
    my_dict = {}
    my_dict['obj'] = result
    return render(request,'restapi/result.html',context=my_dict)

# checks whether any updates on github by a most recent(last) github username searched by customer 
def is_change(request):
    customer_in_session_Fname = request.session.get('customer_obj')['firstName']
    # fetch customer from Customer table in DB using field 'firstName'
    cust_Dao_QS = list(Customer.objects.all().filter(firstName=customer_in_session_Fname).values())
    if cust_Dao_QS:
        cust_obj = cust_Dao_QS[0]
        # if customer has searched atleast 1 github user then make a query to github API as a endpoint and grab response
        if cust_obj['githubUserName'] and cust_obj['activity']: # there are some non-null values in both fields
            api_root_url = "https://api.github.com/users/"
            query_url = api_root_url + cust_obj['githubUserName']
            response = requests.get(query_url)
            result = response.json()
            # return true if there's no new activity in github else false
            if cust_obj['activity'] == result['updated_at']:
                return False
            else:
                return True
    