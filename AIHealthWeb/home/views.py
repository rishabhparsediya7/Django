from django.shortcuts import render, HttpResponse
from home.models import User
def home(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        user=User(firstname=firstname, lastname=lastname, email=email, contact=contact, password=password)
        user.save()
    return render(request, 'signup.html')