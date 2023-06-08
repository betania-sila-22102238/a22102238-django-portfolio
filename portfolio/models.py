from django.db import models

from django.db import models


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
    # Outros campos e relacionamentos relevantes


class Educacao(models.Model):
    curso = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    logotipo_instituicao = models.ImageField(upload_to='logos')
    # Outros campos e relacionamentos relevantes


class Certificado(models.Model):
    titulo = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class OutrasHabilitacoees(models.Model):
    titulo = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class ExperienciaProfissional(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class CompetenciaPessoal(models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class CompetenciaTecnica(models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class CompetenciaOrganizativa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class CompetenciaSocial(models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class CompetenciaLinguistica(models.Model):
    lingua = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    certificacao = models.CharField(max_length=100)
    # Outros campos e relacionamentos relevantes


class InteresseHobby(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    fotografia = models.ImageField(upload_to='interesses_hobbies')
    link = models.URLField()
    # Outros campos e relacionamentos relevantes


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
