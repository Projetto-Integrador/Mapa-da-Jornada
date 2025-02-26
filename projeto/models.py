from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100, default="Informática para Internet", editable=False)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return self.nome

class Modulo(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='modulos')

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    usuario = models.CharField(max_length=100)  # Identificador fictício por agora
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='inscricoes')

    def __str__(self):
        return f"{self.usuario} - {self.disciplina.nome}"

class Topico(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='topicos')
    nome = models.CharField(max_length=100)
    conteudo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome