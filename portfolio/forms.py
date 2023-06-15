from django import forms

from .models import Pagina, Secao, Conteudo, Educacao, Comentario


class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo']

class SecaoForm(forms.ModelForm):
    class Meta:
        model = Secao
        fields = ['titulo', 'pagina']

class ConteudoForm(forms.ModelForm):
    class Meta:
        model = Conteudo
        fields = ['titulo', 'texto', 'secao']
class EducacaoForm(forms.ModelForm):
    class Meta:
        model = Educacao
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }