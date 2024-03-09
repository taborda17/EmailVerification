from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponse
from .models import User
from .forms import Userform
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def login(request):

    page = 'login'

    if request.method == 'POST':        
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            email = request.POST.get(email=email)
        except:
            messages.error(request, 'USER DOES NOT EXIST')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
    context =  {'page':page}
    return render(request, 'loginpage.html',context)

def home(request):
    return render(request,'home.html')

