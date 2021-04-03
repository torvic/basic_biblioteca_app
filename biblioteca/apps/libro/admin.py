from django.contrib import admin
from .models import Autor, Libro

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos','nacionalidad','descripcion','fecha_creacion')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha_publicacion','fecha_creacion')

    

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
