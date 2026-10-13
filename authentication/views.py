from django.shortcuts import render
from django.http import HttpResponse
import authentication
# Create your views here.
def home(request):
    return HttpResponse("<h1>Home url successfully created.<h1>")

def signup(request):
    return render(request, 'authentication/signup.html')

def signin(request):
    return render(request, 'authentication/signin.html')
def signout(request):
    return HttpResponse("Sign out")