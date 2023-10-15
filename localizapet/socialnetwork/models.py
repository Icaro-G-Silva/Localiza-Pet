from django.db import models
from django.contrib.auth.models import get_user_model

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
User = get_user_model()

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O endereço de e-mail é obrigatório.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

class Localizacao(models.Model):
    id = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=30)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)  # Chave estrangeira para o modelo Pet
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Chave estrangeira para o modelo de usuário personalizado
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True, blank=True)  # Chave estrangeira para o modelo de localização
    numero_curtidas = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='posts/', null=False, blank=True)

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    raca = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id  # Você pode retornar o tipo, raça ou qualquer outro campo que identifique o Pet
