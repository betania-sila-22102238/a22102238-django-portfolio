from django.urls import path
from django.contrib.auth import views as auth_views

from portfolio import views

app_name = "portfolio"

urlpatterns = [

    path('index/', views.index_page_view, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto_page_view, name='contacto'),
    path('projetos/', views.projetos_page_view, name='projetos'),
    path('exercicios/', views.exercicios_page_view, name='exercicios'),

    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # Sobre Mim
    path('lista_cadeiras/', views.lista_cadeiras, name='lista_cadeiras'),
    path('cadeira_detalhes/<int:cadeira_id>/', views.cadeira_detalhes, name='cadeira_detalhes'),
    path('adicionar_cadeira/', views.adicionar_cadeira, name='adicionar_cadeira'),
    path('remover_cadeira/<int:cadeira_id>/', views.remover_cadeira, name='remover_cadeira'),
    path('editar_cadeira/<int:cadeira_id>/', views.editar_cadeira, name='editar_cadeira'),

    path('lista_certificados/', views.lista_certificados, name='lista_certificados'),
    path('certificado_detalhes/<int:certificado_id>/', views.certificado_detalhes, name='certificado_detalhes'),
    path('adicionar_certificado/', views.adicionar_certificado, name='adicionar_certificado'),
    path('remover_certificado/<int:certificado_id>/', views.remover_certificado, name='remover_certificado'),
    path('editar_certificado/<int:certificado_id>/', views.editar_certificado, name='editar_certificado'),

    path('educacao/', views.educacao, name='educacao'),
    path('lista_tfc/', views.lista_tfc, name='lista_tfc'),
    path('', views.mais_sobre_mim, name='mais_sobre_mim'),
    path('listar_secoes/', views.listar_secoes, name='listar_secoes'),

    # web
    path('web/', views.web, name='web'),
    path('tecnologias/', views.tecnologias_page_view, name='tecnologias'),
    path('laboratorios/', views.laboratorios, name='laboratorios'),
    path('noticias/', views.noticias, name='noticias'),
    path('sobre/', views.sobre_page_view, name='sobre'),
    path('competencias/', views.competencias, name='competencias'),

    # Registro e autenticação
    path('login_blog', views.login_blog, name='login_blog'),
    path('logout_blog', views.logout_blog, name='logout_blog'),


]
