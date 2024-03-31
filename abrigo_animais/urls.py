from django.contrib import admin
from django.urls import path, include
#from animal.views import mostrar_animais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('animal.urls')),
]
