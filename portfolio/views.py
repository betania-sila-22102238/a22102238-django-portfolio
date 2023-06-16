# Create your views here.
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites import requests
from django.http import HttpResponse

from .forms import SecaoForm, ConteudoForm
from django.shortcuts import render, redirect
from .models import Cadeira, Educacao, Certificado, ExperienciaProfissional, CompetenciaPessoal, CompetenciaTecnica, \
    CompetenciaOrganizativa, CompetenciaSocial, CompetenciaLinguistica, Projeto, TFC, Tecnologia, \
    Secao, Conteudo, Blog, Artigo, Area, Autor, DadosExtraidos


def lista_cadeiras(request):
    cadeiras = Cadeira.objects.all()
    return render(request, 'portfolio/lista_cadeiras.html', {'cadeiras': cadeiras})


def lista_certificados(request):
    certificados = Certificado.objects.all()
    return render(request, 'portfolio/lista_certificados.html', {'certificados': certificados})


def lista_experiencia_profissional(request):
    experiencia_profissional = ExperienciaProfissional.objects.all()
    return render(request, 'portfolio/lista_experiência_profissional.html',
                  {'experiência_profissional': experiencia_profissional})


def lista_competencias_pessoais(request):
    competencias_pessoais = CompetenciaPessoal.objects.all()
    return render(request, 'portfolio/lista_competências_pessoais.html',
                  {'competências_pessoais': competencias_pessoais})


def lista_competencias_tecnicas(request):
    competencias_tecnicas = CompetenciaTecnica.objects.all()
    return render(request, 'portfolio/lista_competências_técnicas.html',
                  {'competências_técnicas': competencias_tecnicas})


def lista_competencias_organizativas(request):
    competencias_organizativas = CompetenciaOrganizativa.objects.all()
    return render(request, 'portfolio/lista_competências_organizativas.html',
                  {'competências_organizativas': competencias_organizativas})


def lista_competencias_sociais(request):
    competencias_sociais = CompetenciaSocial.objects.all()
    return render(request, 'portfolio/lista_competências_sociais.html', {'competências_sociais': competencias_sociais})


def lista_competencias_linguisticas(request):
    competencias_linguisticas = CompetenciaLinguistica.objects.all()
    return render(request, 'portfolio/lista_competências_linguísticas.html',
                  {'competências_linguísticas': competencias_linguisticas})


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
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 2:
                timestamp = cells[0].text
                valor = cells[1].text

                # Armazena os dados no banco de dados
                DadosExtraidos.objects.create(timestamp=timestamp, valor=float(valor))
                dados_obtidos.append({'timestamp': timestamp, 'valor': float(valor)})

        return render(request, 'portfolio/web_scrapping.html', {'dados': dados_obtidos})
    else:
        return HttpResponse("Erro ao fazer a requisição HTTP")
