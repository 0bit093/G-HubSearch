from django.shortcuts import render

import requests

def find_user(request):
    search_user_name = request.POST.get('user_to_find')
    api_root_url = "https://api.github.com/users/"
    # send a request to github api endpoint
    query_url = api_root_url + search_user_name
    # collect response from the endpoint
    response = requests.get(query_url)
    # JSON data
    result = response.json()
    # add the data to dictionary
    my_dict = {}
    my_dict['obj'] = result
    return render(request,'restapi/result.html',context=my_dict)
