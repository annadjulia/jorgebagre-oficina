from django.urls import path
from . import views

urlpatterns = [
    path('', views.pecas, name='pecas'),
    path('new', views.new_peca, name='new_peca'),
    path('<int:id>', views.view_peca, name='view_peca'),
    path('edit/<int:id>', views.edit_peca, name='edit_peca'),
    path('delete/<int:id>', views.delete_peca, name='delete_peca'),
]

