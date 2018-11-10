from django.urls import path
from .views import DepartamentosList

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),

]
