from django import forms
from .models import Pagina, Secao, Conteudo
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
