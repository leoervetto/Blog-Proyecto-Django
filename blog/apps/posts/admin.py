from django.contrib import admin
from .models import categoria, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulo', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')







admin.site.register(categoria)
# Register your models here.
