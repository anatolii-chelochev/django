from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world!")
def index(request):
    return render(request, "hello/index.html")

def prince(request):
    return HttpResponse("Hello, prince!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name}!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })