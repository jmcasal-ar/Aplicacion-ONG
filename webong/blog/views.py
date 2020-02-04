from django.shortcuts import render, get_object_or_404
from .models import Post, Category, User
#Importamos el modelo Post

# Create your views here.
def blog(request):
    post = Post.objects.all()
    #recoletamos todos los posts
    return render(request, "blog/blog.html", {'posts': post})

def category(request, category_id, category_slug):
    category = get_object_or_404(Category, id=category_id)
    #category_id es un campo que se genera automaticamente al momento de crear un registro.
    #Es enviado a nuestra vista por nuestra URL, y lo vamos a utilizar para filtrar.
    #category = Category.objects.get(id= category_id) FORMA SIMPLE DE HACERLO.
    #FORMA ELEGANTE DE EN CASO DE ERROR USAR UN 404
    #get permite recoger un unico registro, filtrando por id.
    #posts = Post.objects.filter(categories=category) #filtramos por categoria
    #return render(request, "blog/category.html", {'category': category, 'posts': posts})
    #Forma atajo mágico:
    return render(request, "blog/category.html", {'category': category})

def blogSingle(request, post_id, post_slug):
    post = get_object_or_404(Post, id=post_id)
    categorias = Category.objects.all()
    return render(request, 'blog/blog-single.html', {'post':post, 'categorias': categorias})

def author(request, author_id, author_slug):
    author = get_object_or_404(User, id=user_id)
    #category_id es un campo que se genera automaticamente al momento de crear un registro.
    #Es enviado a nuestra vista por nuestra URL, y lo vamos a utilizar para filtrar.
    #category = Category.objects.get(id= category_id) FORMA SIMPLE DE HACERLO.
    #FORMA ELEGANTE DE EN CASO DE ERROR USAR UN 404
    #get permite recoger un unico registro, filtrando por id.
    #posts = Post.objects.filter(categories=category) #filtramos por categoria
    #return render(request, "blog/category.html", {'category': category, 'posts': posts})
    #Forma atajo mágico:
    return render(request, "blog/author.html", {'author': author})