from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home url successfully created.<h1>")

def signup(request):
    return HttpResponse("<h1>Sign up page<h1>")

def signin(request):
    return HttpResponse("<h1>Sign in page<h1>")

def signout(request):
    pass