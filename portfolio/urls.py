#  hello/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "portfolio"
urlpatterns = [

    path('', views.index_page_view, name='index'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('exercicios', views.exercicios_page_view, name='exercicios'),
    path('conteudo', views.criar_conteudo, name='conteudo'),
    path('pagina', views.criar_pagina, name='pagina'),

    # URLs de autenticação
    path('login', auth_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view, name='logout'),
    path('register/', views.register, name='register'),

    # Sobre Mim
    path('lista_cadeiras', views.lista_cadeiras, name='lista_cadeiras'),
    path('educacao', views.educacao, name='educacao'),
    path('lista_certificados', views.lista_certificados, name='lista_certificados'),
    path('lista_certificados', views.lista_experiencia_profissional, name='lista_experiencia_profisional'),
    path('lista_competencias_linguisticas', views.lista_competencias_linguisticas, name='lista_competencias_linguisticas'),
    path('lista_competencias_organizativas', views.lista_competencias_organizativas, name='lista_competencias_organizativas'),
    path('lista_competencias_pessoais', views.lista_competencias_pessoais, name='lista_competencias_pessoais'),
    path('lista_competencias_sociais', views.lista_competencias_sociais, name='lista_competencias_sociais'),
    path('lista_tfc', views.lista_tfc, name='lista_tfc'),
    path('lista_interesses_hobbies', views.lista_interesses_hobbies, name='lista_interesses_hobbies'),
    path('listar_secoes', views.listar_secoes, name='listar_secoes'),

    #web
    path('web', views.web, name='web'),
    path('tecnologias', views.tecnologias_page_view, name='tecnologias'),
    path('backend', views.backend_page_view, name='backend'),
    path('frontend', views.frontend_page_view, name='frontend'),
    path('laboratorios',views.laboratorios,name='laboratorios'),
    path('noticias', views.noticias, name= 'noticias'),
    path('exemplos_e_tecnicas',views.exemplos_e_tecnicas, name='exemplos_e_tecnicas'),
    path('quizz',views.quizz,name='quizz'),
    path('sobre', views.sobre_page_view, name='sobre'),
]
