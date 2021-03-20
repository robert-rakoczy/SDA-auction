from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

def loginpage(request):
    return render(request, 'accounts/login.html')

def registerpage(request):
    return render(request, 'accounts/register.html')

def home(request):
    return render(request, "home.html")

def products(request):
    return render(request,"products.html")