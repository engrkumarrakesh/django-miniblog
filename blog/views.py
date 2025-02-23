from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.urls import reverse


# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'home.html',{'post':post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        return render(request, 'dashboard.html', {'posts':post})
    else:
        return HttpResponseRedirect('/login/')
      
def signup(request):    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Signed Up!')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    # messages.success(request, 'Successfully Logged In!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
            # messages.error(request, 'Invalid Credentials! Please Try Again.')
        return render (request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    # messages.success(request, 'Successfully Logged Out!')
    return HttpResponseRedirect('/')

# CREATE NEW POSTS
def createpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Successfully Created!')
                    return HttpResponseRedirect('/dashboard/')
                except:
                    messages.error(request, 'Failed to Create!')
        else:
            form = PostForm()
        return render(request, 'createpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


# UPDATE EXISTING POSTS
def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Successfully Updated!')
                    return HttpResponseRedirect('/dashboard/')
                except:
                    messages.error(request, 'Failed to Update!')
        else:
            form = PostForm(instance=get)
        return render(request, 'updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

# DELETE EXISTING POSTS
def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(id=id)
            try:
                post.delete()
                messages.success(request, 'Successfully Deleted!')
                return HttpResponseRedirect('/dashboard/')
            except:
                messages.error(request, 'Failed to Delete!')
                return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')