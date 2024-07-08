from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from .forms import SecaoForm, ConteudoForm, AdicionarCadeiraForm, CertificadoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadeira, Educacao, Certificado, Projeto, TFC, Tecnologia, \
    Secao, Conteudo, Blog, Artigo, Area, Autor, Competencia, Cidade


def lista_cadeiras(request):
    cadeiras = Cadeira.objects.all()
    return render(request, 'portfolio/lista_cadeiras.html', {'cadeiras': cadeiras})


def remover_cadeira(request, cadeira_id):
    cadeira = get_object_or_404(Cadeira, pk=cadeira_id)
    cadeira.delete()
    return redirect('portfolio:lista_cadeiras')


def remover_certificado(request, certificado_id):
    certificado = get_object_or_404(Certificado, pk=certificado_id)
    certificado.delete()
    return redirect('portfolio:lista_certificados')


def cadeira_detalhes(request, cadeira_id):
    cadeira = get_object_or_404(Cadeira, pk=cadeira_id)
    return render(request, 'portfolio/detalhes_cadeira.html', {'cadeira': cadeira})


def certificado_detalhes(request, certificado_id):
    certificado = get_object_or_404(Certificado, pk=certificado_id)
    return render(request, 'portfolio/detalhes_certificado.html', {'certificado': certificado})


def editar_cadeira(request, cadeira_id):
    cadeira = get_object_or_404(Cadeira, pk=cadeira_id)

    if request.method == 'POST':
        form = AdicionarCadeiraForm(request.POST, instance=cadeira)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_cadeiras')
    else:
        form = AdicionarCadeiraForm(instance=cadeira)

    return render(request, 'portfolio/editar_cadeira.html', {'form': form, 'cadeira': cadeira})


def editar_certificado(request, certificado_id):
    certificado = get_object_or_404(Cadeira, pk=certificado_id)

    if request.method == 'POST':
        form = CertificadoForm(request.POST, instance=certificado)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_certificados')
    else:
        form = CertificadoForm(instance=certificado)

    return render(request, 'portfolio/editar_certificado.html', {'form': form, 'certificado': certificado})


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
            return redirect('portfolio:listar_conteúdos')
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


def laboratorios(request):
    return render(request, 'portfolio/laboratorios.html')


def noticias(request):
    return render(request, 'portfolio/noticias.html')


def educacao(request):
    context = {'formacoes': Educacao.objects.all()}
    return render(request, 'portfolio/educacao.html', context)


def cadeira(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/lista_cadeiras.html', context)


def adicionar_cadeira(request):
    if request.method == 'POST':
        form = AdicionarCadeiraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'portfolio:lista_cadeiras')  # Redirecionar para a página de listagem de cadeiras após adicionar
    else:
        form = AdicionarCadeiraForm()
    return render(request, 'portfolio/adicionar_cadeira.html', {'form': form})


def editar_cadeira_view(request, cadeira_id):
    cadeira = get_object_or_404(Cadeira, id=cadeira_id)
    if request.method == 'POST':
        form = AdicionarCadeiraForm(request.POST, request.FILES, instance=cadeira)
        if form.is_valid():
            form.save()
            return redirect('portfolio:detalhes_cadeira', cadeira_id=cadeira.id)
    else:
        form = AdicionarCadeiraForm(instance=cadeira)
    return render(request, 'portfolio/editar_cadeira.html', {'form': form, 'cadeira': cadeira})


def login_blog(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portifolio:home_blog_full')
        else:
            # aqui
            return render(request, 'portfolio/blog/login_blog.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/blog/login_blog.html')


def logout_blog(request):
    logout(request)
    return redirect('portifolio:home_blog_full')


def blog(request):
    blog = Blog.objects.first()
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


def competencias(request):
    competencias = Competencia.objects.all()

    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def adicionar_certificado(request):
    if request.method == 'POST':
        form = CertificadoForm(request.POST,
                               request.FILES)  # Certifique-se de incluir 'request.FILES' para processar a imagem
        if form.is_valid():
            certificado = form.save(commit=False)  # Salve o formulário, mas não o banco de dados ainda
            certificado.user = request.user  # Associe o usuário atual (se estiver autenticado) ao certificado
            certificado.save()  # Agora salve no banco de dados com o usuário associado
            return redirect(
                'portfolio:lista_certificados')  # Redirecione para a página de listagem de certificados após adicionar
    else:
        form = CertificadoForm()

    return render(request, 'portfolio/adicionar_certificado.html', {'form': form})
