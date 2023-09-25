from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "first/index.html")

def kia(request):
  return HttpResponse("Hello, Kia")

def greet(request, name):
  return render(request, "first/greet.html", {
    "name": name.capitalize() 
  })