import pandas as pd

def conciliar_bancos(arquivo_entrada, arquivo_saida):
    # Carregar dados do arquivo Excel
    extrato_df = pd.read_excel(arquivo_entrada, sheet_name='Extrato')
    registro_df = pd.read_excel(arquivo_entrada, sheet_name='Registro')

    # Realizar a conciliação bancária
    conciliacao_df = pd.DataFrame(columns=['Data', 'Descrição', 'Valor (R$)', 'Diferença (R$)'])
    for index, extrato_row in extrato_df.iterrows():
        registro_row = registro_df.iloc[index]
        
        if extrato_row['Data'] != registro_row['Data']:
            return "Erro: As datas no extrato e no registro interno não correspondem."
        
        diferenca = extrato_row['Valor (R$)'] - registro_row['Valor (R$)']
        conciliacao_df = conciliacao_df.append({
            'Data': extrato_row['Data'],
            'Descrição': extrato_row['Descrição'],
            'Valor (R$)': extrato_row['Valor (R$)'],
            'Diferença (R$)': diferenca
        }, ignore_index=True)

    # Salvar resultados em uma nova planilha Excel
    with pd.ExcelWriter(arquivo_saida) as writer:
        conciliacao_df.to_excel(writer, sheet_name='Conciliação', index=False)

    return "Conciliação concluída. Resultados salvos em: " + arquivo_saida

# Nome dos arquivos de entrada e saída
arquivo_entrada = 'transacoes_bancarias.xlsx'
arquivo_saida = 'conciliacao.xlsx'

# Chamar a função para conciliar os bancos
resultado = conciliar_bancos(arquivo_entrada, arquivo_saida)
print(resultado)
