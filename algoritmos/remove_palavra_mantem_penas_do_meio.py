import pandas as pd

# Corrigindo o caminho do arquivo
caminho_arquivo = 'C:/Users/roger/python/Pasta7.xlsx'

# Carregue o arquivo Excel
df = pd.read_excel(caminho_arquivo)

# Função para manter o que está entre as palavras
def manter_entre_palavras(texto):
    palavras = str(texto).split()
    if len(palavras) >= 3:
        resultado = ' '.join(palavras[1:-1])
    else:
        resultado = texto
    return resultado

# Substitua 'SuaColuna' pelo nome real da sua coluna
nome_coluna = 'Coluna1'

# Aplicar a função à coluna desejada
df['Nome'] = df[nome_coluna].apply(manter_entre_palavras)

# Salvar o DataFrame de volta no arquivo Excel
df.to_excel('novoArquivo3.xlsx', index=False)
