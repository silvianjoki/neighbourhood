from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http  import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Profile, Neighbourhood,Business,Post
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def home(request):
    
    
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.all()
    
    return render(request, 'profile.html',{ 'profile':profile})


@login_required(login_url='/accounts/login/')
def add_post(request):
    
    
    return render(request, 'add_post.html')