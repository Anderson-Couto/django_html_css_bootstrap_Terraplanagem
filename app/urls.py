from django.urls import path

from .views import index, orcamento, contato

urlpatterns = [
    path('', index, name='index'),
    path('orcamento', orcamento, name='orcamento'),
    path('contato', contato, name='contato'),
]