from django.urls import path
from . import views

urlpatterns = [
    path('', views.ordens, name='ordens'),
    path('new', views.new_ordem, name='new_ordem'),
    path('<int:id>', views.view_ordem, name='view_ordem'),
    path('edit/<int:id>', views.edit_ordem, name='edit_ordem'),
    path('delete/<int:id>', views.delete_ordem, name='delete_ordem'),
]

