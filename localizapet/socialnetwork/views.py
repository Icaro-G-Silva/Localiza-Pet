from django.shortcuts import render

def home(request):
    # Implemente a view para a página inicial (feed de notícias, por exemplo)
    return render(request, 'socialnetwork/home.html')

def profile(request, username):
    # Implemente a view para os perfis de usuário
    return render(request, 'socialnetwork/profile.html')
