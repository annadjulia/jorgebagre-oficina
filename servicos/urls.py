from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicos, name='servicos'),
    path('new', views.new_servico, name='new_servico'),
    path('<int:id>', views.view_servico, name='view_servico'),
    path('edit/<int:id>', views.edit_servico, name='edit_servico'),
    path('delete/<int:id>', views.delete_servico, name='delete_servico'),
]

