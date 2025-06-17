from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import handler404
from rest_framework_simplejwt.tokens import RefreshToken
from users.tasks import send_custom_mail

# This is the view that handle signup for user
def SignupView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # check if password matches to the confirmation password
        if password!=confirm_password:
            messages.error(request,"Password donot match")
            return render(request,'signup_page.html')

        if not password:
            messages.error(request, "Password is required")
            return render(request, 'signup_page.html')

        # check if length of password is not less than 8
        required_length = 8
        if len(password) < required_length:
           messages.error(request,"password is too short")
           return render(request, 'signup_page.html')

        # check if email is already used
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already taken")
            return render(request,'signup_page.html')

        # create a username from email
        username = email.split('@')[0]

        # create a new User
        User.objects.create_user(username = username,email=email,password=password)

        # Using celery  sends an registration mail after registration is success
        send_custom_mail.delay(email,username,password)
        # Authenticate user and return boolen value None
        user = authenticate(request,username=username,password=password)

        # login and Redirect to the homepage After successfull account creation
        if user is not None:
            login(request,user)
            return redirect('homepage')
    return render(request,'signup_page.html')

# This is the view that handle login logics
def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request,'login_page.html')

# This is the view that handle homepage
def HomeView(request):
    username = request.user.username
    return render(request,'home_page.html',{'username':username})

# This view Handles logout logic
@login_required(login_url='/login/')
def LogoutView(request):
    logout(request)
    return redirect('loginpage')

# This is the view that handles undeclared url
def custom_404_view(request):
    return render(request, '404.html',status = 404)