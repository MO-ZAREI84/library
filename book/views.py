from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Author
from .forms import AuthorForm
from django.views import View
from django.views.generic import ListView
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
    