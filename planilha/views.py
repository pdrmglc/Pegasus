from django.shortcuts import render, redirect
from .forms import PlanilhaForm
import pandas as pd
import matplotlib.pyplot as plt
import os
from urllib.parse import urljoin
from django.conf import settings
import python_plots

# Create your views here.

def home(request):

    static_url = settings.STATIC_URL

    return render(request, 'index.html', {'static_url':static_url})

def templates(request):

    static_url = settings.STATIC_URL

    return render(request, "templates.html", {'static_url':static_url})

def upload_planilha(request):

    static_url = settings.STATIC_URL

    if request.method == 'POST':
        form = PlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            planilha = form.cleaned_data['arquivo']

            # Gere um nome de arquivo único usando uuid
            nome_arquivo = f"planilha.xlsx"

            # Caminho absoluto para salvar a planilha no servidor
            caminho_arquivo = os.path.join(settings.MEDIA_ROOT, "planilhas",nome_arquivo)

            # Salve a planilha no servidor
            with open(caminho_arquivo, 'wb') as arquivo:
                for parte in planilha.chunks():
                    arquivo.write(parte)

            request.session['caminho_arquivo'] = caminho_arquivo

            return redirect('exibir_grafico')
    else:
        form = PlanilhaForm()
    return render(request, 'upload_planilha.html', {'form': form, 'static_url':static_url})

def exibir_grafico(request):

    static_url = settings.STATIC_URL
    
    tipo_grafico = request.POST.get('tipo_grafico')
    # Processar a planilha e criar o gráfico usando o caminho do arquivo
    caminho_arquivo = request.session.get('caminho_arquivo')

    data_sheet = pd.read_excel(caminho_arquivo, sheet_name="data")
    design_sheet = pd.read_excel(caminho_arquivo, sheet_name="design")
    settings_sheet = pd.read_excel(caminho_arquivo, sheet_name="settings")

    # Crie o caminho absoluto para salvar o gráfico na pasta "media"
    media_root = os.path.join(settings.BASE_DIR, 'media')
    graph_path = os.path.join(media_root, 'grafico.png')

    python_plots.ploter(data_sheet, design_sheet, settings_sheet, graph_path)


    # Crie o URL correto para a imagem de mídia usando urljoin
    media_url = settings.MEDIA_URL
    graph_url = urljoin(media_url, 'grafico.png')

    return render(request, 'exibir_grafico.html', {'graph_url': graph_url, 'static_url':static_url})
