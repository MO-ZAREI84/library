from django.shortcuts import render
from django.http import HttpResponse
# fvb 
def welecom(request):
    return HttpResponse('hello')