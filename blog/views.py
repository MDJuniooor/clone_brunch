from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.user.

def signin(request):
    return render(request, 'blog/signin.html')

def signout(request):
    return render(request, 'blog/signout.html')

