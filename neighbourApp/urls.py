from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from . import views





urlpatterns=[
    re_path('^$', views.index, name = 'index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_business/', views.add_business, name='add_business'),
    path('search/', views.search, name= 'search'),
    path('neighbourhood/', views.neighbourhood, name = 'neighbourhood')
    
    
    

]















if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)