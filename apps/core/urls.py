from django.urls import path
from .views import home, celery

urlpatterns = [
    path('', home, name='home'),
    path('celery/', celery, name='celery'),
]
