from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http  import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
    
    return render(request, 'profile.html',{ 'profile':profile})


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


