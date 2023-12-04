from django.urls import path
from . import views

urlpatterns = [
    path('', views.veiculos, name='veiculos'),
    path('new', views.new_veiculo, name='new_veiculo'),
    path('<int:id>', views.view_veiculo, name='view_veiculo'),
    path('edit/<int:id>', views.edit_veiculo, name='edit_veiculo'),
    path('delete/<int:id>', views.delete_veiculo, name='delete_veiculo'),
]

