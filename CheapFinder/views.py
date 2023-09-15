from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("CheapFinder is a system for finding products with cheap price.")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def home(request):
    return HttpResponse("Welcome to CheapFinder")