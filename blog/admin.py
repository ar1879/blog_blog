

from django.contrib import admin

from . models import *
from import_export import resources
from import_export.admin  import ImportExportModelAdmin

# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'estado', 'fecha_creacion']
    resource_class = CategoriaResource


#############################################################################

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor    



class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'email']
    list_display = ['nombres', 'apellidos', 'email', 'estado', 'fecha_creacion']
    resource_class = AutorResource

#############################################################################

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo', 'slug', 'descripcion']
    list_display = ['titulo', 'slug', 'descripcion', 'fecha_creacion']
    resource_class = PostResource      

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)