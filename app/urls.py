from django.urls import path
from . import views

urlpatterns = [
    path('tecnologia/', views.lista_tecnologia, name='lista_tecnologia'),
    path('vestuario/', views.lista_vestuario, name='lista_vestuario'),
    path('produto/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
]
