from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pavan(request):
    return HttpResponse('<h1><marquee>MY NAME IS PAVAN IS GOOD BOY</h1></marquee>')
