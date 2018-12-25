from django.db import models


class Teste(models.Model):
    descricao = models.TextField()


class RegistroUsuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        db_table = 'registro_usuarios'

