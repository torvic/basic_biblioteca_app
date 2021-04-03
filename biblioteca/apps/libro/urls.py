from django.urls import path
from . import views 

urlpatterns = [
    path('crear_autor/', views.crearAutor, name='crear_autor')
]