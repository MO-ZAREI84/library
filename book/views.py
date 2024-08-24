from django.shortcuts import render
from django.http import HttpResponse
# fvb 
def Hello(request,first_name,age):
    return HttpResponse(f'hello {first_name} your age is {age}')