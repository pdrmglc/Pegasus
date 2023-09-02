from django.shortcuts import render, redirect
from .forms import PlanilhaForm
import pandas as pd
import matplotlib.pyplot as plt
import os
from urllib.parse import urljoin
from django.conf import settings
import uuid

# Create your views here.

def home(request):
    return render(request, 'home.html')

def upload_planilha(request):
    if request.method == 'POST':
        form = PlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            planilha = form.cleaned_data['arquivo']

            # Gere um nome de arquivo único usando uuid
            nome_arquivo = f"planilha_{uuid.uuid4()}.xlsx"

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
    return render(request, 'upload_planilha.html', {'form': form})

def exibir_grafico(request):
    # Processar a planilha e criar o gráfico usando o caminho do arquivo
    caminho_arquivo = request.session.get('caminho_arquivo')
    df = pd.read_excel(caminho_arquivo)

    # Salvar o gráfico em um arquivo temporário
    plt.bar(df['Nome'], df['Valor'])
    plt.xlabel('Nome')
    plt.ylabel('Valor')
    plt.title('Gráfico de Barras')

    # Crie o caminho absoluto para salvar o gráfico na pasta "media"
    media_root = os.path.join(settings.BASE_DIR, 'media')
    graph_path = os.path.join(media_root, 'grafico.png')

    # Salve o gráfico no caminho absoluto
    plt.savefig(graph_path)
    plt.close()

    # Crie o URL correto para a imagem de mídia usando urljoin
    media_url = settings.MEDIA_URL
    graph_url = urljoin(media_url, 'grafico.png')

    return render(request, 'exibir_grafico.html', {'graph_url': graph_url})
