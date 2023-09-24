from django.shortcuts import render
from .models import Post  # Importe o modelo de postagem (se você tiver um)

def home(request):
    # Obtém todas as postagens do banco de dados (exemplo)
    posts = Post.objects.all()  # Substitua "Post" pelo seu modelo de postagem

    context = {
        'posts': posts,
    }

    return render(request, 'socialnetwork/home.html', context)
