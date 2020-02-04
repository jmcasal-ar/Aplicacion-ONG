from django import template
from blog.models import Post

#Registramos el archivo como template
register = template.Library()

#Creamos metodo para obtener todas las paginas. El @ es un decorador para registrar nuestra funcion como simple tag
@register.simple_tag
def get_post_list():
    posts = Post.objects.all()
    return posts


