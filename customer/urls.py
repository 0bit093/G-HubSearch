from django.urls import path, include
from customer import views

urlpatterns = [
    # takes to login/home page
    path('',views.login_page,name='login_page'),
    # when user clicks on link sign-up in login page
    path('sign_up/',views.sign_up,name='sign_up'),
    # after sign-up button click control comes here
    path('create/',views.createCustomer,name='create_customer'),
    # to validate customer
    path('home/',views.validateCustomer,name='validateCustomer'),
    # linking a path to restapi urls
    path('',include('restapi.urls')),
    # displays customer info like email,fname etc
    path('show/', views.showCustomerInfo, name='showCustomerInfo'),
    # sign off the customer
    path('logout/',views.logout_view,name='logout'),
    # show user page pre-filled with info for updating details
    path('update_info_/',views.show_update_page_view,name='update_info_page'),
    # after updating details login with new email & pass
    path('login/',views.new_login_page,name='new_login_page'),
    # shows page for customer to confirm deletion by prompting to enter pswd
    path('delete/',views.confirm_delete_page,name='confirm_delete_customer'),
    # deletes the customer
    path('delete_account/',views.deleteCustomer, name='delete_customer'),
]
