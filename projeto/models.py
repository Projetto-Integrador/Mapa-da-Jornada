from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)  # Relacionamento com o Curso


    def __str__(self):
        return self.nome