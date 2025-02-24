from django.db import models

class Curso(models.Model):
    nome = models.CharField(
        max_length=100, 
        default="Informática para Internet", 
        editable=False  # Impede que seja alterado no admin ou em formulários
    )
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField() # Campo de texto
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)  # Relacionamento com o Curso


    def __str__(self):
        return self.nome


class Modulo(models.Model):
    disciplina = models.ForeignKey(
        Disciplina, 
        on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=255)
    ordem = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - Ordem {self.ordem} (Disciplina: {self.disciplina.nome})"

class Topico(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='topicos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()  # Este é o campo 'descricao' que você está tentando usar

    def __str__(self):
        return self.nome