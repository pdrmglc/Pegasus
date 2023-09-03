import pandas as pd
import matplotlib.pyplot as plt


def ploter(data_sheet, design_sheet, settings_sheet, graph_path):
    
    design_sheet['valor_opcao'] = design_sheet['valor_opcao'].fillna("")
    settings_sheet['valor_config'] = settings_sheet['valor_config'].fillna("")

    dic_design = {opcao: valor_opcao for opcao, valor_opcao in zip(design_sheet["opcao"], design_sheet["valor_opcao"])}
    dic_settings = {config: valor_config for config, valor_config in zip(settings_sheet["config"], settings_sheet["valor_config"])}

    if dic_settings['plot'] == "bar":

        plt.bar(data_sheet['Nome'], data_sheet['Valor'])
        plt.xlabel(dic_design['nome_eixo_x'])
        plt.ylabel(dic_design['nome_eixo_y'])
        plt.title(dic_design['titulo'])

    elif dic_settings['plot'] == "pie":

        plt.pie(data_sheet['Valor'], labels=data_sheet['Nome'])
        plt.title(dic_design['titulo'])
    

    plt.savefig(graph_path, dpi=dic_settings['dpi'])
    plt.close()