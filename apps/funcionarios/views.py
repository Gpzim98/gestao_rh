from django.views.generic import ListView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario
