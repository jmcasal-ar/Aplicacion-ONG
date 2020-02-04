from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Visualizamos columnas en el panel. El __ se usa para campos relacionales
    list_display = ('title', 'author', 'published', 'post_categories')
    #ordenamos el panel
    ordering = ('author', 'published' ) 
    #agregamos una caja de busqueda por los siguientes campos
    search_fields = ('title', 'content', 'author_usernmane', 'categories_name')
    #agregamos un panel de visualización por jerarquia
    date_hierarchy = 'published'
    #agregamos filtros para buscar
    list_filter = ("author__username", "categories__name")

    def post_categories(self, obj):
        #Clase para agregar la columna categoria al list_display
        #self siempre tiene q estar en una clase, y obj es q recorra cada objeto como una fila
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)