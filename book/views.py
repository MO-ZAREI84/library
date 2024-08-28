from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Author
from .forms import AuthorForm
from django.views import View
from django.views.generic import ListView
from rest_framework.decorators import api_view
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from rest_framework.response import Response
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def Hello(request, first_name, age):
    return HttpResponse(f'hello {first_name} your age is {age}')

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

@csrf_exempt
def Authors(request):
    if request.method == 'GET':
        authors = Author.objects.values()
        return render(request, 'authors.html', {'Authors': authors})
    
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return HttpResponse('is not valid')
        
        name = form.cleaned_data['name']
        Author.objects.create(name=name)
        return HttpResponse(f'author created {name=}')
    
    return HttpResponse('method not allowed')

@csrf_exempt

def new_authors(request):
    if request.method == 'GET':
        authors_form = AuthorForm()  # تغییر نام متغیر برای وضوح
        return render(request, 'new_authors.html', {'authors_form': authors_form})

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return HttpResponse(form.errors)
        
        name = form.cleaned_data['name']
        Author.objects.create(name=name)
        return HttpResponse(f'your authors are created {name=}')
    
    return HttpResponse('method not allowed')
def Author_list(request):
    authors=Authors.objects.all()
    return render(request,'authors_list.html',{
        'authors':authors
    })
class HelloView(View):
    def get(self,request):
       return HttpResponse('hello')
class AuthorListView(ListView):
    model=Author
    template_name='author_list_view.html'
    # default context is object_list 
    context_object_name='authors'
    paginate_by=3
@csrf_exempt
@api_view(['GET'])
def library (request,library_id):
    library=Library.objects.get(id=library_id)
    
    if request.method =='GET':
        response={"id":library.id,"number":library.number}
        return Response(data=response)
    if request.method == 'DELETE':
        library.delete()
        return HttpResponse('delet')

def user_list(request):
    if request.user.is_authenticated:
        users=User.objects.all()
        return render(request,'user_list.html',{'users':users})
    return HttpResponse('your not login')
def register(request):
    if request.method == 'GET':
        form=UserCreationForm
        return render(request,'register.html',{'form':form})
    elif request.method=='POST':
        form=UserCreationForm(request.POST)
        if not form.is_valid():
            render(request,'register.html',{'form':form})
        form.save()
        return HttpResponse('user created')
    return HttpResponse('method is not allowed')
def login(request):
    # تعریف فرم به عنوان یک متغیر خالی برای هر دو حالت
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return HttpResponse('users')  # یا هر URL دیگری که بعد از ورود به آن بروید
    
    # در هر دو حالت GET و POST فرم به قالب ارسال می‌شود
    return render(request, 'login2.html', {'form': form})