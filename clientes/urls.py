from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('new', views.new_cliente, name='new_cliente'),
    path('<int:id>', views.view_cliente, name='view_cliente'),
    path('edit/<int:id>', views.edit_cliente, name='edit_cliente'),
    path('delete/<int:id>', views.delete_cliente, name='delete_cliente'),
]

