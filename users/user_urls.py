""" This is the urls file for user app """
from django.urls import path
from users.views import SignupView,LoginView,LogoutView,HomeView
urlpatterns = [
    path('signup/',SignupView,name='signuppage'),
    path('login/',LoginView,name='loginpage'),
    path('logout/',LogoutView,name='logout'),
    path('',HomeView,name='homepage')
]