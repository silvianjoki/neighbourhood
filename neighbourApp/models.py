from django.db import models
from django.contrib.auth.models import User


class Neighbourhood(models.Model):
    n_name= models.CharField(max_length=255)
    location= models.CharField(max_length=255)
    occupants= models.IntegerField()
    admin=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.location
    
    def create_neighbourhood(self):
        return self.save()
    
    def delete_neighbourhood(self):
        self.delete()
    
    @classmethod
    def find_neighbourhood(cls,id):
        return cls.objects.filter(id=id)
    
    @classmethod
    def update_neighbourhood(cls,id, name):
        return cls.objects.filter(id=id).update(name=name)
    
    @classmethod
    def update_occupants(cls, id, name):
        return cls.objects.filter(id=id).update(name=name)
    


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name= models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to = 'images/', null=True)
    
    
    def __str__(self):
        return self.user.username
    
    def save_admin(self):
        self.save()

    def delete_profile(self):
        self.delete() 



class Profile(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.CharField(max_length=255)
    n_name = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    profile_id = models.IntegerField()
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete() 
        


class Business(models.Model):
    name= models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    n_name= models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email=models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username
    
    def create_business(self):
        self.save()
        
    @classmethod
    def find_business(cls,id):
        return cls.objects.filter(id=id)
    
    @classmethod
    def update_business(cls,id, name):
        return cls.objects.filter(id=id).update(name=name)
