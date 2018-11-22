from .models import RegistroHoraExtra
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
