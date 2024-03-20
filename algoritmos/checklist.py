import tkinter as tk
from datetime import datetime

# Criar a janela principal
root = tk.Tk()

# Criar uma lista para armazenar os itens do checklist
checklist = []

# Função para adicionar um item ao checklist
def add_item():
    item = entry.get()
    if item != "":
        checklist.append(item)
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

# Criar um campo de entrada de texto
entry = tk.Entry(root)
entry.pack()

# Criar um botão para adicionar itens
add_button = tk.Button(root, text="Adicionar item", command=add_item)
add_button.pack()

#Criar um botão para deletar
add_button = tk.Button(root, text="Deletar", command=add_item)
add_button.pack()

#Inicia a Hora da tarefa.
add_button = tk.Button(root, text="Inicio da Tarefa", command=add_item)
add_button.pack()


# Criar uma lista para exibir os itens
listbox = tk.Listbox(root)
listbox.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()
