from urllib import request
from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    queryset = request.GET.get('buscar')#buscar hace referencia a el parametro name del index.html nombrado de la misma manera
    print(queryset)#aqui estamos pidiendo ver lo que se le esta pasando como parametro al GET
    post = Post.objects.filter(estado = True)
    if queryset:
        post = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset) | Q(fecha_creacion__icontains = queryset)).distinct()

    paginator = Paginator(post, 2)     
    page = request.GET.get('page')   
    post = paginator.get_page(page)
        
    return render(request, 'index.html', {'post':post})
    '''en la linea 12 se usan los objetos Q dentro de un filter y lo que hay dentro de cada objeto Q es lo que queremos usar como base para hacer nuestras busquedas es decir si buscamos por titulo tendremos tendremos una respuesta de igual manera si buscamos por descripcion en este caso si buscamos por autor no nos devolvera una respuesta ya que no hay ningun filtro que haga referencia a ese campo'''

def detallePosts(request,slug):
    posts = get_object_or_404(Post,slug = slug)
    print(posts)
    return render(request, 'post.html', {'detalle_post':posts})    

def generales(request):
    queryset = request.GET.get('buscar')
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'General'))
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset),
            estado = True, categoria = Categoria.objects.get(nombre__iexact = 'General')).distinct()
    paginator = Paginator(post, 2)     
    page = request.GET.get('page')   
    post = paginator.get_page(page)            
    return render(request, 'generales.html', {'post':post})

def programacion(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programacion'))
    paginator = Paginator(post, 2)     
    page = request.GET.get('page')   
    post = paginator.get_page(page)
    return render(request, 'programacion.html', {'post':post})

def videojuegos(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'))
    paginator = Paginator(post, 2)     
    page = request.GET.get('page')   
    post = paginator.get_page(page)
    return render(request, 'videojuegos.html', {'post':post})        

def tutoriales(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    paginator = Paginator(post, 2)     
    page = request.GET.get('page')   
    post = paginator.get_page(page)
    return render(request, 'tutoriales.html',{'post':post})   

