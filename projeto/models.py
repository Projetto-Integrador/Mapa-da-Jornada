from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.PositiveIntegerField()  
    
    def __str__(self):
        return self.nome
