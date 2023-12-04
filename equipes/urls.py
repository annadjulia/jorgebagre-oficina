from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipes, name='equipes'),
    path('new', views.new_equipe, name='new_equipe'),
    path('<int:id>', views.view_equipe, name='view_equipe'),
    path('edit/<int:id>', views.edit_equipe, name='edit_equipe'),
    path('delete/<int:id>', views.delete_equipe, name='delete_equipe'),
]

