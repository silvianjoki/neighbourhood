from django import forms
from .models import Profile,Post, Neighbourhood, Business


class ProfileForm(forms.ModelForm):
    model = Profile
    class  Meta:
        model = Profile
        exclude = ['n_name']
        

class NeighbourhoodForm(forms.ModelForm):
    model = Neighbourhood
    class  Meta:
        model = Neighbourhood
        exclude = ['admin']
        

class PostForm(forms.ModelForm):
    model = Post
    class  Meta:
        model = Post
        exclude = ['']
        
        
class BusinessForm(forms.ModelForm):
    model = Business
    class  Meta:
        model = Business
        exclude = [ 'user']
        
        


