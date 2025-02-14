from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(1500)
    duracao = models.PositiveIntegerField()  
    
    def __str__(self):
        return f"{self.nome} - {self.descricao} - {self.duracao}"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(1500)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.descricao} - {self.carga_horaria}"


class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(1500)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='arquivos/') #inserir arquivo no diretório arquivos 
    
    def __str__(self):
        return f"{self.nome} - {self.descricao}"
  

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.nome} - {self.email}"

class AlunoCurso(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.aluno} - {self.curso}"

