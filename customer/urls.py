from django.urls import path, include
from customer import views

urlpatterns = [
    # takes to login/home page
    path('',views.login_page),
    # when user clicks on link sign-up in login page
    path('sign_up/',views.sign_up,name='sign_up'),
    # after sign-up button click control comes here
    path('create/',views.createCustomer,name='create_customer'),
    # to validate customer
    path('validate/',views.validateCustomer,name='validateCustomer'),

    # linking a path to restapi urls
    path('',include('restapi.urls')),

    # path('main_page/',views.main_page,name='main_page'),

]
