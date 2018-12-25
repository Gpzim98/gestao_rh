from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from apps.funcionarios.models import Funcionario


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_relatorio():
    total = Funcionario.objects.all().count()
    send_mail(
        'Relatorio Celery',
        'Relatorio geral de funcionarios %f' % total,
        'django@gregorypacheco.com.br',
        ['openshift@gregorypacheco.com.br'],
        fail_silently=False,
    )

    return 'Email sent'
