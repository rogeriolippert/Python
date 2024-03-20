import pandas as pd

# Corrigindo o caminho do arquivo
caminho_arquivo = 'C:/Users/roger/python/Pasta7.xlsx'

# Carregue o arquivo Excel
df = pd.read_excel(caminho_arquivo)

# Função para remover o que está entre as palavras
def remover_entre_palavras(texto):
    palavras = str(texto).split()
    if len(palavras) >= 3:
        resultado = palavras[0] + ' ' + palavras[-1]
    else:
        resultado = texto
    return resultado

# Substitua 'SuaColuna' pelo nome real da sua coluna
nome_coluna = 'Coluna1'

# Aplicar a função à coluna desejada
df['Nome'] = df[nome_coluna].apply(remover_entre_palavras)

# Salvar o DataFrame de volta no arquivo Excel
df.to_excel('BasicTamanho.xlsx', index=False)
