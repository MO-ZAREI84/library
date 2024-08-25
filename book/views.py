from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Book
# fvb 
def Hello(request,first_name,age):
    return HttpResponse(f'hello {first_name} your age is {age}')
def index(request):
    book=Book.objects.get(id=5)
    return render (request,'index.html',{'book':book})