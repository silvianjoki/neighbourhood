from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http  import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from requests import post
from .forms import PostForm, ProfileForm, BusinessForm, NeighbourhoodForm

from .models import Profile, Neighbourhood,Business,Post
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    post = Post.objects.all()
    neighbourhood = Neighbourhood.objects.all()
    business=Business.objects.all()
    profile = Profile.objects.all()
    
    return render(request, 'home.html', {'current_user':current_user,'business':business, 'post':post,'neighbourhood':neighbourhood, 'profile':profile})

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.all()
    post = Post.objects.all()
    current_user = request.user
    
    if request.method == ' POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.name = current_user
            profile.save()
        else:
            form = ProfileForm()
    return render(request, 'profile.html',{ 'profile':profile, 'post':post})


@login_required(login_url='/accounts/login/')
def add_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'add_post.html', {'form': form })


@login_required(login_url='/accounts/login/')
def add_business(request):
    current_user = request.user
    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.save(commit=False)
            name.profile = current_user
            name.save()
        return redirect('home')
    else:
        form = BusinessForm()
    
    return render(request, 'add_business.html', {'form': form })


@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    current_user = request.user
    if request.method == "POST":
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.profile = current_user
            location.save()
        return redirect('home')
    else:
        form = Neighbourhood()
    
    return render(request, 'neighbourhood.html', {'form': form })

@login_required(login_url='/accounts/login/')
def search(request):
    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        neighbourhood = request.GET.get('neighbourhood')
        searchname= Post.search_by_neighbourhood(neighbourhood)
        message = f"{neighbourhood}"
        return render(request, 'search.html',{"message":message, "neighbourhood":searchname})
    else:
        return render(request, 'search.html')