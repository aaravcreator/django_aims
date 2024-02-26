from django.shortcuts import render,redirect

from .models import Author
from .forms import AuthorFilterForm,AuthorForm,LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    context = {}
    return render(request,'blog/index.html',context)


def loginPage(request):
    error = None
    form = LoginForm()
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('author_list')
        else:
            error = "Username or Password error"
    context = {
        'form':form,
        'error':error
    }
    return render(request,'blog/login.html',context)


def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def author_list(request):
    if not  request.user.is_authenticated:
        return redirect('loginPage')
    form = AuthorFilterForm()
    name = request.GET.get('name')
    if name is not None:
        authors = Author.objects.filter(name__contains = name).order_by('-id')
    else:
        authors = Author.objects.all().order_by('-id')
    # authors = Author.objects.filter(age__gt=10)
    print(authors)


    context = {
        'author_list':authors,
        'form':form,

    }
    return render(request,'blog/author_list.html',context)

def create_author(request):
    if not  request.user.is_authenticated:
        return redirect('loginPage')
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() ## creates author in the database
            return redirect('author_list')
    context ={
        'form':form
    }
    return render(request,'blog/create_author.html',context)

def edit_author(request,id):
    author = Author.objects.get(id=id)
    form = AuthorForm(instance=author)
    if request.method == "POST":
        form = AuthorForm(request.POST,request.FILES,instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')

    context = {
        'form':form
    }
    return render(request,'blog/edit_author.html',context)


def delete_author(request,id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.delete()
        return redirect('author_list')
    context = {
        'author':author
    }
    return render(request,'blog/delete_author.html',context)