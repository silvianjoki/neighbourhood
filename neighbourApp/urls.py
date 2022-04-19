from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from . import views





urlpatterns=[

    
    
    

]















if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)