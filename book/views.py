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
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializer import BookSerializer
from rest_framework import status
from rest_framework.mixins import  ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView

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
    if request.method =='GET':
        form = AuthenticationForm()
        return render(request, 'login2.html', {'form': form})
        
        
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if not form.is_valid():
            return render(request, 'login2.html', {'form': form}) 
        user=form.get_user()
        auth_login(request, user)
        return HttpResponse('your loged in')  # یا هر URL دیگری که بعد از ورود به آن بروید
                
    # در هر دو حالت GET و POST فرم به قالب ارسال می‌شود
def change_password(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first')

        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if not request.user.check_password(old_password):
            return HttpResponse('Wrong old password')

        if new_password1 != new_password2:
            return HttpResponse('Entered passwords are not identical')

        request.user.set_password(new_password1)
        request.user.save()

        return HttpResponse('Password changed successfully!')

    return HttpResponse('Only post method allowed')
class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.get("name")
        author = data.get("author")
        book = Book.objects.create(name=name, author=author) # ساختن کتاب
        serializer = BookSerializer(book) # ترجمه به json
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class BookListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)