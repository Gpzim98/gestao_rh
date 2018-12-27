from django.db import models
from django.urls import reverse


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')

    @property
    def total_funcionarios(self):
        return self.funcionario_set.all().count()

    @property
    def total_funcionarios_ferias(self):
        return self.funcionario_set.filter(de_ferias=True).count()

    @property
    def total_funcionarios_doc_pendente(self):
        return self.funcionario_set.filter(documento=None).count()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('home')
