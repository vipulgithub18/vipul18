from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student(request):
    return HttpResponse("<h1>This is my best page <h1>")
