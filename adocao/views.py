from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from adocao.forms import AdotanteForm, SolicitacaoAdocaoForm
from adocao.models import SolicitacaoAdocao
from animal.models import Animal

def home_adocao(request):
    animais_disponiveis = Animal.objects.filter(adotado=False)
    return render(request, 'home_adocao.html', {'animais': animais_disponiveis})

def cadastro_adotante(request):
    mensagem = None
    if request.method == 'POST':
        form = AdotanteForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem = "Cadastro efetuado com sucesso!"
    else:
        form = AdotanteForm()
    contexto = {
        'form': form,
        'mensagem': mensagem
    }
    return render(request, 'cadastro_adotante.html', contexto)

@login_required
def solicitar_adocao(request):
    sucesso = False
    if request.method == 'POST':
        form = SolicitacaoAdocaoForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.adotante = request.user.adotante
            solicitacao.save()
            sucesso = True
            return redirect('confirmacao_adocao')
    else:
        form = SolicitacaoAdocaoForm()
    animais_disponiveis = Animal.objects.filter(adotado=False)
    contexto = {
        'form': form,
        'sucesso': sucesso,
        'animais_disponiveis': animais_disponiveis
    }
    return render(request, 'solicitar_adocao.html', contexto)

def confirmacao_adocao(request):
    return render(request, 'confirmacao_adocao.html')

@login_required
def consultar_status(request):
    status = SolicitacaoAdocao.objects.filter(adotante=request.user)
    return render(request, 'consultar_status.html', {'status': status})

class login_adotante(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Usuário autenticado com sucesso!')
        else:
            return HttpResponse('Falha na autenticação do usuário.')