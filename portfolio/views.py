# Create your views here.
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import os
import requests
from django.http import HttpResponseRedirect

from .forms import SecaoForm, ConteudoForm
from django.shortcuts import render, redirect, HttpResponse
from .models import Cadeira, Educacao, Certificado, ExperienciaProfissional, Projeto, TFC, Tecnologia, \
    Secao, Conteudo, Blog, Artigo, Area, Autor, DadosExtraidos, Question, Choice, Competencia


def lista_cadeiras(request):
    cadeiras = Cadeira.objects.all()
    return render(request, 'portfolio/lista_cadeiras.html', {'cadeiras': cadeiras})


def lista_certificados(request):
    certificados = Certificado.objects.all()
    return render(request, 'portfolio/lista_certificados.html', {'certificados': certificados})



def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/lista_projetos.html', {'projetos': projetos})


def lista_tfc(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/lista_tfc.html', {'tfcs': tfcs})


def web(request):
    web = Tecnologia.objects.all()
    return render(request, 'portfolio/web.html', {'web': web})


def lista_tecnologias(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/lista_tecnologias.html', {'tecnologias': tecnologias})


def layout_page_view(request):
    return render(request, 'portfolio/layout.html')


def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')


def tecnologias_page_view(request):
    return render(request, 'portfolio/tecnologias.html')


def exercicios_page_view(request):
    return render(request, 'portfolio/exerciciosJavaScript.html')


def index_page_view(request):
    return render(request, 'portfolio/index.html')


def frontend_page_view(request):
    return render(request, 'portfolio/frontend.html')


def backend_page_view(request):
    return render(request, 'portfolio/backend.html')


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


def sobre_page_view(request):
    return render(request, 'portfolio/sobre_este_website.html')


def mais_sobre_mim(request):
    return render(request, 'portfolio/mais_sobre_mim.html')


def criar_secao(request):
    if request.method == 'POST':
        form = SecaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_seções')
    else:
        form = SecaoForm()
    return render(request, 'portfolio/criar_secao.html', {'form': form})


def editar_Secao(request, pk):
    secao = Secao.objects.get(pk=pk)
    if request.method == 'POST':
        form = SecaoForm(request.POST, instance=secao)
        if form.is_valid():
            form.save()
            return redirect('listar_seções')
    else:
        form = SecaoForm(instance=secao)
    return render(request, 'portfolio/editar_secao.html', {'form': form})


def apagar_secao(request, pk):
    secao = Secao.objects.get(pk=pk)
    secao.delete()
    return redirect('listar_seções')


def listar_secoes(request):
    secoes = Secao.objects.all()
    return render(request, 'portfolio/listar_seções.html', {'seções': secoes})


# Funções para Conteúdo

def criar_conteudo(request):
    if request.method == 'POST':
        form = ConteudoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_conteúdos')
    else:
        form = ConteudoForm()
    return render(request, 'portfolio/criar_conteúdo.html', {'form': form})


def editar_conteudo(request, pk):
    conteudo = Conteudo.objects.get(pk=pk)
    if request.method == 'POST':
        form = ConteudoForm(request.POST, instance=conteudo)
        if form.is_valid():
            form.save()
            return redirect('listar_conteúdos')
    else:
        form = ConteudoForm(instance=conteudo)
    return render(request, 'portfolio/editar_conteúdo.html', {'form': form})


def apagar_conteudo(request, pk):
    conteudo = Conteudo.objects.get(pk=pk)
    conteudo.delete()
    return redirect('listar_conteúdos')


def listar_conteudos(request):
    conteudos = Conteudo.objects.all()
    return render(request, 'portfolio/listar_conteúdos.html', {'conteúdos': conteudos})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'portfolio/register.html', {'form': form})


@login_required
def minha_visualizacao_protegida(request):
    # Acesso a dados, processamento, ou outras operações relacionadas à sua lógica de negócio
    usuario = request.user  # Acessa o objeto do usuário autenticado
    dados = {
        'usuario': usuario.username,
        'mensagem': 'Bem-vindo à sua visualização protegida!'
    }

    # Renderiza o template 'minha_visualizacao_protegida.html' com os dados processados
    return render(request, 'portfolio/minha_visualizacao_protegida.html', context=dados)


def laboratorios(request):
    return render(request, 'portfolio/laboratorios.html')


def noticias(request):
    return render(request, 'portfolio/noticias.html')


def exemplos_e_tecnicas(request):
    return render(request, 'portfolio/exemplos_e_tecnicas.html')


def quizz(request):
    return render(request, 'portfolio/quizz.html')


def educacao(request):
    context = {'formacoes': Educacao.objects.all()}
    return render(request, 'portfolio/educacao.html', context)


def cadeira(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/lista_cadeiras.html', context)


def blog(request):
    blog = Blog.objects.first()  # Obtém o primeiro blog (você pode ajustar isso conforme necessário)
    areas = Area.objects.all()
    autores = Autor.objects.all()
    artigos = Artigo.objects.all()

    context = {
        'blog': blog,
        'areas': areas,
        'autores': autores,
        'artigos': artigos,
    }

    return render(request, 'portfolio/blog.html', context)


def web_scrapping(request):
    url = "https://www.publico.pt"

    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        # Extraia os dados do web scraping
        # Substitua esta parte do código de acordo com a estrutura do site e os dados que deseja extrair
        dados_obtidos = []
        # Exemplo: Extrai os valores de uma tabela
        table = soup.find('table')
        if table is not None:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    timestamp = cells[0].text
                    valor = cells[1].text

                    # Armazena os dados no banco de dados
                    DadosExtraidos.objects.create(timestamp=timestamp, valor=float(valor))
                    dados_obtidos.append({'timestamp': timestamp, 'valor': float(valor)})

            else:
                return HttpResponse("Erro ao fazer a requisição HTTP", status=response.status_code)


def labs(request, lab):
    lab_path = os.path.join('portfolio', 'static', 'portfolio', 'labs', lab)
    lab_files = os.listdir(lab_path)
    lab_images = [file for file in lab_files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    lab_videos = [file for file in lab_files if file.endswith(('.mp4', '.avi', '.mov'))]
    context = {
        'lab': lab,
        'lab_files': lab_files,
        'lab_images': lab_images,
        'lab_videos': lab_videos
    }
    return render(request, 'portfolio/laboratorios.html', context)


def quiz(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'portfolio/quiz.html', context)

def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(str(question.id), None)
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        context = {'score': score}
        return render(request, 'portfolio/result.html', context)
    return HttpResponseRedirect('/quiz/')

def competencias(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})