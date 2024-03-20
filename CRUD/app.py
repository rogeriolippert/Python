from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)
excel_file = 'dados.xlsx'

def carregar_dados():
    try:
        df = pd.read_excel(excel_file)
        return df.to_dict('records')
    except FileNotFoundError:
        return []

def salvar_dados(dados):
    df = pd.DataFrame(dados)
    df.to_excel(excel_file, index=False)

@app.route('/')
def index():
    dados = carregar_dados()
    return render_template('index.html', dados=dados)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    dados = carregar_dados()
    novo_registro = {
        'Nome': request.form['nome'],
        'Idade': request.form['idade'],
        'Endereço': request.form['endereco'],
        'Nº': request.form['num'],
        'Bairro': request.form['bairro'],
        'Cidade': request.form['cidade'],
        'Estado': request.form['uf'],
        'CPF': request.form['cpf'],
        'Telefone': request.form['telefone']
    }
    dados.append(novo_registro)
    salvar_dados(dados)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
