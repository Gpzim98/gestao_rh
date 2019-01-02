from django.urls import path
from .views import home, celery, filtra_funcionarios, departamentos_ajax

urlpatterns = [
    path('', home, name='home'),
    path('celery/', celery, name='celery'),
    path('departamentos-ajax/', departamentos_ajax, name='departamentos_ajax'),
    path('filtra-funcionarios/', filtra_funcionarios, name='filtra_funcionarios'),
]
