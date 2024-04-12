from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('animal.urls', namespace='animais')),  
    path('adocao/', include('adocao.urls', namespace='adocao')),    
    path('voluntarios/', include('voluntarios.urls', namespace='voluntarios')),      
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)