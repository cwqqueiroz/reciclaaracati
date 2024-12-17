from django import forms

from .models import Coleta, Material, Dia

class ColetaForm(forms.ModelForm):
    class Meta:
        model = Coleta
        fields = ['rua', 'numero', 'bairro', 'materiais', 'dias', 'turno']
        widgets = {
            'rua': forms.TextInput(attrs={'placeholder': 'Digite sua rua e número'}),
            'numero': forms.TextInput(attrs={'placeholder': 'Digite o seu telefone'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Digite seu bairro'}),
            'materiais': forms.CheckboxSelectMultiple(),
            'dias': forms.CheckboxSelectMultiple(),
            'turno': forms.RadioSelect(),
        }