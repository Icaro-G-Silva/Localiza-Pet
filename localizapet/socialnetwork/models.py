from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_lost_or_found = models.DateField()  # Data de perda ou encontro do animal
    location = models.CharField(max_length=200)  # Localização do animal
    # Adicione outros campos conforme necessário

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Imagem de perfil do usuário
    # Adicione campos adicionais do perfil do usuário conforme necessário

class Post(models.Model):
    # Campo para a imagem (pode usar o modelo FileField para fazer upload)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    # Campo para a descrição
    description = models.TextField()

    # Campo para a localização
    location = models.CharField(max_length=255)

    # Campo para a raça
    race = models.CharField(max_length=100)

    # Campo para o tipo (por exemplo, cão, gato, etc.)
    type = models.CharField(max_length=50)

    # Campo para a cor
    color = models.CharField(max_length=50)

    # Campo para associar o post a um usuário (se desejar)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Campo para a data de criação do post (automática)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post de {self.user.username} em {self.created_at}"