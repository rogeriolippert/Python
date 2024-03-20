import time

class Tarefa:
    def __init__(self):
        self.tarefas = {}

    def criar(self, nome):
        self.tarefas[nome] = {'inicio': time.time(), 'fim': None, 'tempo_gasto': None}

    def finalizar(self, nome):
        self.tarefas[nome]['fim'] = time.time()
        self.tarefas[nome]['tempo_gasto'] = self.tarefas[nome]['fim'] - self.tarefas[nome]['inicio']

    def ler(self, nome):
        return self.tarefas.get(nome, None)

    def atualizar(self, nome, novo_nome):
        if nome in self.tarefas:
            self.tarefas[novo_nome] = self.tarefas.pop(nome)

    def deletar(self, nome):
        if nome in self.tarefas:
            del self.tarefas[nome]

# Exemplo de uso
tarefa = Tarefa()
tarefa.criar('Tarefa 1')
time.sleep(80)  # Simula o tempo gasto na tarefa
tarefa.finalizar('Tarefa 1')
print(tarefa.ler('Tarefa 1'))