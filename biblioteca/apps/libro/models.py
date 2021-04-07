from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombres',max_length=200,blank=False,null=False)
    apellidos = models.CharField('Apellidos',max_length=220,blank=False,null=False)
    nacionalidad = models.CharField('Nacionalidad',max_length=100,blank=False,null=False)
    descripcion = models.TextField('Descripcion',blank=True,null=True)
    estado = models.BooleanField('Estado',default=True)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True,auto_now_add=False)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('titulo',max_length=255,blank=False,null=False)
    fecha_publicacion = models.DateField('Fecha de publicacion',blank=False,null=False)
    autor_id = models.ManyToManyField(Autor,related_name='groups')
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo