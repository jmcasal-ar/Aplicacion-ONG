from django.urls import path
from . import views

urlpatterns = [

    #Paths del Blog
    path('blog/', views.blog, name="blog"),
    path ('blog/<int:post_id>/<slug:post_slug>/', views.blogSingle, name="blogSingle"),
    path ('blog/category/<int:category_id>/<slug:category_slug>/', views.category, name="category"),
    path ('blog/author/<int:author_id>/<slug:author_slug>/', views.author, name="auhtor"),
    #<>/ es un campo dinamico. Con eso pasamos un parametro, que la url pasará a la vista como category_id
    #Es importante que se pasa como cadena de caracteres. Como necesitamos que sea un int (xq el id es un int)
    #agregamos int: para castear.
]