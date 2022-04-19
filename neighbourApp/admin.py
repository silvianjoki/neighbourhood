from django.contrib import admin

# Register your models here.
from .models import Profile, Business, Post, Admin, Neighbourhood

admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Admin)
admin.site.register(Neighbourhood)
