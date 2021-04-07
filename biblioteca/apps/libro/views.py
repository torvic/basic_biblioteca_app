from django.shortcuts import render, redirect,get_object_or_404 
from .forms import AutorForm
from .models import Autor

def Home(request):
    return render(request,'index.html')

def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
        print(autor_form)

    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores = Autor.objects.filter(estado=True)

    return render(request,'libro/listar_autor.html',{'autores':autores})

def editarAutor(request, id):
    #autor = Autor.objects.get(id=id)
    autor = get_object_or_404(Autor,id=id)
    
    if request.method == 'GET':
        autor_form = AutorForm(instance = autor)
    else:
        autor_form = AutorForm(request.POST, instance = autor)
        if autor_form.is_valid():
            autor_form.save()
        return redirect('index')
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})

def eliminarAutor(request, id):
    # ELIMINACION 
    """ autor = get_object_or_404(Autor,id=id)
    autor.delete()
    return redirect('libro:listar_autor') """
    #ELIMINACION DIRECTA (ELIMINAS DE LA DB)
    """ autor = get_object_or_404(Autor,id=id)
    
    if request.method == 'POST':
        autor.delete()
        return redirect('libro:listar_autor')
    
    return render(request,'libro/eliminar_autor.html',{'autor':autor}) """
    #ELIMINACION LOGICA (NO ELIMINAS DE LA DB)
    autor = get_object_or_404(Autor,id=id)

    if request.method == "POST":
        autor.estado = False
        autor.save()

        return redirect('libro:listar_autor')
    
    return render(request,'libro/eliminar_autor.html',{'autor':autor})