from django.urls import path, include
from customer import views

urlpatterns = [
    # takes to login/home page
    path('',views.login_page),
    path('main_page/',views.main_page,name='main_page'),
]
