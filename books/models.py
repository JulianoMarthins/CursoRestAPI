from tkinter import PAGES
from uuid import uuid4
from django.db import models

# Create your models here.


class Books(models.Model):

    id_book = models.UUIDField(
        primary_key=True, default=uuid4(), editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=255)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)


"""
        
    id_book utilizada o método 'UUIDField', este método é responsável por 
gerar automáticamente uma Id ao livro, para cada objeto criado pelo usuário

    Em seus parâmetros, temos inicialmente o 'primay_key', este está sendo
definido como verdadeiro para que esta ID seja armazenada no banco de dados
como chave primária

    Default=uuid4() é a padronização o tipo de id que será gerada durante a
criação do objetgo.

    Editable sendo verdadeira, proibe que esta chave gerada seja editada,
tornando esta única e imutável.

        
"""
