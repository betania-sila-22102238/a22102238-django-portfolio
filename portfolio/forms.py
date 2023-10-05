from django import forms

from .models import Pagina, Secao, Conteudo, Educacao, Comentario, Cadeira


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


class AdicionarCadeiraForm(forms.ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'  # Isso permite que todos os campos do modelo sejam incluídos no formulário