from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('faturamento/', views.faturamento, name='faturamento'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
]