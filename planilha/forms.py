from django import forms
from .models import Planilha

class PlanilhaForm(forms.ModelForm):
    
    tipos = [
        ('barra', 'Gráfico de Barras'),
        ('pizza', 'Gráfico de Pizza'),
        ('linha', 'Gráfico de Linha'),
        # Adicione outros tipos de gráfico conforme necessário
    ]

    tipo_grafico = forms.ChoiceField(choices=tipos, label='Escolha o Tipo de Gráfico')  # Substitua TIPOS_GRAFICO pelas opções desejadas

    class Meta:
        model = Planilha
        fields = ('arquivo',)