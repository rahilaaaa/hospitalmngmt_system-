from django.shortcuts import render, redirect
from . models import Departments,Doctor
from .forms import BookingForm,ContactForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    
    return render(request,'home.html')

@login_required(login_url='login')
def About(request):
    return render(request,'about.html')

@login_required(login_url='login')
def Booking(request):
   if request.method == 'POST':
       form = BookingForm(request.POST)
       if form.is_valid():
           form.save()
           return render(request,'confirmation.html')
   form = BookingForm()
   dict_from ={
       'form' : form
   }
   return render(request,'booking.html',dict_from)

@login_required(login_url='login')
def Doctors(request):
    dict_docs = {
        'doctors': Doctor.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

@login_required(login_url='login')
def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'thankyou.html')
    form = ContactForm()
    dict_form ={
       'form':form
    }
    return render(request,'contact.html',dict_form)

@login_required(login_url='login')
def Department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect URL after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect back to login page with error message
    else:
        return render(request, 'login.html')





def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('signup')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'You are now registered and can log in')
        return redirect('login')
    else:
        return render(request, 'signup.html')
    
def Logout(request):
    logout(request)
    return redirect('login')
