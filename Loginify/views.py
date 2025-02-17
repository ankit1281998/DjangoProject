from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetails
from django.contrib import messages

def print_hello(request):
    return HttpResponse('Hello World!')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(Email=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('/loginify/signup/')
    
        new_user = UserDetails(Username=username, Email=email, Password=password)
        new_user.save()
        
        messages.success(request, 'Signup successful! Please log in.')
        return redirect('/loginify/login/')
    
    return render(request, 'Loginify/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = UserDetails.objects.get(Email=email)
            
            if user.Password == password:
                messages.success(request, 'Login successful!')
                return redirect('/loginify/home/')  
            else:
                messages.error(request, 'Invalid password.')
                return redirect('/loginify/login/')
        
        except UserDetails.DoesNotExist:
            messages.error(request, 'No user found with this email.')
            return redirect('/loginify/login/')
    
    return render(request, 'Loginify/login.html')

def home(request):
    return render(request, 'Loginify/home.html')