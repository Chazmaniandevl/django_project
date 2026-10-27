from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Portfolio Home Page")

def index(request):
    return render(request,'portfolio_app/index.html')
