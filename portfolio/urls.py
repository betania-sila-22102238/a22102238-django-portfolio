from django.urls import path
from django.contrib.auth import views as auth_views

from portfolio import views

app_name = "portfolio"
urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto_page_view, name='contacto'),
    path('projetos/', views.projetos_page_view, name='projetos'),
    path('exercicios/', views.exercicios_page_view, name='exercicios'),
    path('web_scrapping/', views.web_scrapping, name='web_scrapping'),
    path('labs/', views.labs, name='labs'),

    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # Sobre Mim
    path('lista_cadeiras/', views.lista_cadeiras, name='lista_cadeiras'),
    path('educacao/', views.educacao, name='educacao'),
    path('lista_certificados/', views.lista_certificados, name='lista_certificados'),
    path('lista_tfc/', views.lista_tfc, name='lista_tfc'),
    path('mais_sobre_mim/', views.mais_sobre_mim, name='mais_sobre_mim'),
    path('listar_secoes/', views.listar_secoes, name='listar_secoes'),

    # web
    path('web/', views.web, name='web'),
    path('tecnologias/', views.tecnologias_page_view, name='tecnologias'),
    path('backend/', views.backend_page_view, name='backend'),
    path('frontend/', views.frontend_page_view, name='frontend'),
    path('laboratorios/', views.laboratorios, name='laboratorios'),
    path('noticias/', views.noticias, name='noticias'),
    path('exemplos_e_tecnicas/', views.exemplos_e_tecnicas, name='exemplos_e_tecnicas'),
    path('quiz/', views.quiz, name='quiz'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('sobre/', views.sobre_page_view, name='sobre'),
    path('competencias/', views.competencias, name='competencias'),
]
