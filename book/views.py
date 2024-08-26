from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Book,Author
from .forms import AuthorForm
# fvb 
def Hello(request,first_name,age):
    return HttpResponse(f'hello {first_name} your age is {age}')
def index(request):
    book=Book.objects.all()
    return render (request,'index.html',{'books':book})
@csrf_exempt
def Authors(request):
    if request.method=='GET':
        authors=Author.objects.values()
        return render(request,'author.html',{'Authors':authors})
    
    if request.method=='POST':
        form= AuthorForm(request.POST)
        if  not form.is_valid():
            HttpResponse('is not valid')
        name=form.cleaned_data['name']
        Author.objects.create(name=name)
        return HttpResponse(f'author created {name=}')
    return HttpResponse('method not allowed')