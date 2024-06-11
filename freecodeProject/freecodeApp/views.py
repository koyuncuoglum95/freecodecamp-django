from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def index(request):
    products = Product.objects.all().values()

    context = {
        'products': products
    }

    # print(context)
    return render(request, 'index.html', context)

def counter(request):
    # words = request.POST['words']
    # amount_of_words = len(words.split())

    posts = [1,2,3,4,5,'tim','tom','john']
    context = {
        # 'amount': amount_of_words,
        'posts': posts
    }
    return render(request, 'counter.html', context)


def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pwd']
        rpassword = request.POST['rpwd']

        if password == rpassword:
            if User.objects.filter(username=uname).exists():
                messages.error(request, "User already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, email=email, password=password)
                user.save()
                messages.success(request, 'User is successfully registered')
                return redirect('login')
        else:
            messages.error('Credentials Invalid')
            return redirect('register')
        
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pwd']

        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
    
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('index')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})