from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Admin
from ordens.models import Ordem
from django.db.models import Sum

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        senha = request.POST.get('senha')

        resp = Admin.objects.filter(user=user, senha=senha)

        if user == ' ' or senha == ' ':
            print('Os campos não podem ficar vazios.')
            return render(request, 'login.html', {'msg': 'Os campos não podem ficar vazios.'})
        else:
            print('Login realizado com sucesso!')
            return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def dashboard(request):
    ordens = Ordem.objects.all()
    if ordens:
        numOrdens = ordens.count()
        totalOrdens = ordens.aggregate(total=Sum('valor'))['total']
    else:
        numOrdens = 0
        totalOrdens = 0
    return render(request, 'dashboard.html', {'ordens': ordens, 'numOrdens': numOrdens, 'totalOrdens': totalOrdens})

def faturamento(request):
    
        return render(request, 'faturamento.html')

def configuracoes(request):
        
            return render(request, 'configuracoes.html')