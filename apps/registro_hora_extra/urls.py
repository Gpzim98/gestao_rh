from django.urls import path
from .views import (
    HoraExtraList,
    # FuncionarioEdit,
    # FuncionarioDelete,
    # FuncionarioNovo
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    # path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    # path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
