
# Register your models here.
from django.contrib import admin
from .models import Blog,DonoBlog, Autor, Area, Artigo, Comentario, Like, Educacao

admin.site.register(Blog)
admin.site.register(DonoBlog)
admin.site.register(Autor)
admin.site.register(Area)
admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Like)
admin.site.register(Educacao)
