from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)

    def str (self):
        return self.nome
