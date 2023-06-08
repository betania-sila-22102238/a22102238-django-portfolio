#  hello/urls.py
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.layout_page_view, name='layout'),
    path('index', views.index_page_view, name='index'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('tecnologias', views.tecnologias_page_view, name='tecnologias'),
    path('backend', views.backend_page_view, name='backend'),
    path('frontend', views.frontend_page_view, name='frontend'),
    path('exercicios', views.exercicios_page_view, name='exercicios')
]
