from django.urls import path
from . import views

urlpatterns = [
    path('', views.mecanicos, name='mecanicos'),
    path('new', views.new_mecanico, name='new_mecanico'),
    path('<int:id>', views.view_mecanico, name='view_mecanico'),
    path('edit/<int:id>', views.edit_mecanico, name='edit_mecanico'),
    path('delete/<int:id>', views.delete_mecanico, name='delete_mecanico'),
]

