from django.shortcuts import render
from django.http import HttpResponse


def calculate(request):
    return HttpResponse("Hello World - calculate")


def home(request):
    return HttpResponse("Hello World!")
