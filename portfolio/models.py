from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.shortcuts import redirect


class Blog(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class DonoBlog(models.Model):
    nome = models.CharField(max_length=100)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Area(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField()
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


class Like(models.Model):
    TIPO_CHOICES = (
        ('LIKE', 'Like'),
        ('DISLIKE', 'Dislike'),
    )

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo


class Cadeira(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ano_letivo_frequentado = models.IntegerField()
    topicos_abordados = models.TextField()

class Educacao(models.Model):
    curso = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    logotipo_instituicao = models.ImageField()

    def is_valid(self):
        try:
            self.clean_fields()
            self.clean()
        except ValidationError:
            return False
        return True


class Certificado(models.Model):
    titulo = models.CharField(max_length=100)


class OutrasHabilitacoees(models.Model):
    titulo = models.CharField(max_length=100)


class ExperienciaProfissional(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos')
    ano_realizacao = models.IntegerField()
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    participantes = models.ManyToManyField('Pessoa')
    link_repositorio = models.URLField()
    link_video = models.URLField()
    # Outros campos e relacionamentos relevantes


class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField('Pessoa', related_name='tfc_autores')
    orientadores = models.ManyToManyField('Pessoa', related_name='tfc_orientadores')
    ano_realizacao = models.IntegerField()
    imagem = models.ImageField(upload_to='tfc')
    resumo = models.TextField()
    link_relatorio = models.URLField()
    link_repositorio = models.URLField()
    link_video = models.URLField()
    # Outros campos e relacionamentos relevantes


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()
    criador = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='logotipos_tecnologias')
    link_site_oficial = models.URLField()
    linguagens_usadas = models.CharField(max_length=100)
    descricao = models.TextField()
    # Outros campos e relacionamentos relevantes


class Pagina(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Secao(models.Model):
    titulo = models.CharField(max_length=100)
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Conteudo(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class DadosExtraidos(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    valor = models.FloatField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
