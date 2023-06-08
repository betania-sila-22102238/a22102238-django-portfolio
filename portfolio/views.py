# Create your views here.

from django.shortcuts import render
from .models import Cadeira, Educacao, Certificado, ExperienciaProfissional, CompetenciaPessoal, CompetenciaTecnica, \
    CompetenciaOrganizativa, CompetenciaSocial, CompetenciaLinguistica, InteresseHobby, Projeto, TFC, Tecnologia


def lista_cadeiras(request):
    cadeiras = Cadeira.objects.all()
    return render(request, 'portfolio/lista_cadeiras.html', {'cadeiras': cadeiras})


def lista_educacao(request):
    educacao = Educacao.objects.all()
    return render(request, 'portfolio/lista_educação.html', {'educação': educacao})


def lista_certificados(request):
    certificados = Certificado.objects.all()
    return render(request, 'portfolio/lista_certificados.html', {'certificados': certificados})


def lista_experiencia_profissional(request):
    experiencia_profissional = ExperienciaProfissional.objects.all()
    return render(request, 'portfolio/lista_experiência_profissional.html',
                  {'experiência_profissional': experiencia_profissional})


def lista_competencias_pessoais(request):
    competencias_pessoais = CompetenciaPessoal.objects.all()
    return render(request, 'portfolio/lista_competências_pessoais.html', {'competências_pessoais': competencias_pessoais})


def lista_competencias_tecnicas(request):
    competencias_tecnicas = CompetenciaTecnica.objects.all()
    return render(request, 'portfolio/lista_competências_técnicas.html', {'competências_técnicas': competencias_tecnicas})


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


def lista_interesses_hobbies(request):
    interesses_hobbies = InteresseHobby.objects.all()
    return render(request, 'portfolio/lista_interesses_hobbies.html', {'interesses_hobbies': interesses_hobbies})


def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/lista_projetos.html', {'projetos': projetos})


def lista_tfc(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/lista_tfc.html', {'tfcs': tfcs})


def lista_tecnologias(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/lista_tecnologias.html', {'tecnologias': tecnologias})


# Outras views e funcionalidades relacionadas


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
    return render(request, 'portfolio/sobre.html')
