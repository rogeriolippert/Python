import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

class AplicativoProcessamento(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Processamento de Arquivo Excel")

        self.caminho_arquivo = None
        self.nome_coluna = None

        self.configurar_interface()

    def configurar_interface(self):
        tk.Label(self, text="Selecione o arquivo Excel:").pack(pady=10)
        tk.Button(self, text="Selecionar Arquivo", command=self.selecionar_arquivo).pack(pady=5)

        tk.Label(self, text="Digite o nome da coluna a ser processada:").pack(pady=5)
        self.entry_coluna = tk.Entry(self)
        self.entry_coluna.pack(pady=10)

        tk.Button(self, text="Processar", command=self.processar_arquivo).pack(pady=10)

    def selecionar_arquivo(self):
        self.caminho_arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx;*.xls")]
        )

    def processar_arquivo(self):
        if not self.caminho_arquivo:
            messagebox.showerror("Erro", "Selecione um arquivo Excel.")
            return

        self.nome_coluna = self.entry_coluna.get()

        if not self.nome_coluna:
            messagebox.showerror("Erro", "Digite o nome da coluna.")
            return

        df = pd.read_excel(self.caminho_arquivo)
        df['Nome'] = df[self.nome_coluna].apply(self.remover_entre_palavras)
        df.to_excel('novo_arquivo01.xlsx', index=False)

        messagebox.showinfo("Concluído", "Processamento concluído. Verifique o arquivo 'novo_arquivo.xlsx'.")

    def remover_entre_palavras(self, texto):
        palavras = str(texto).split()
        if len(palavras) >= 3:
            resultado = palavras[0] + ' ' + palavras[-1]
        else:
            resultado = texto
        return resultado

if __name__ == "__main__":
    app = AplicativoProcessamento()
    app.mainloop()

