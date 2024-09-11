from flask import Flask
app = Flask (__name__)
usuario= "usuario1"
@app.route('/')
def index():
    return "Estilo do Rei Barbearia"

@app.route('/novofuncionario')
def adicionar_funcionario():
    return"Funcionario ADICIONADO"

@app.route('/novocliente')
def adicionar_cliente():
    return"Cliente ADICIONADO"

@app.route('/novoservico')
def adicionar_serviço():
    return"serviço ADICIONADO"

@app.route('/novoagendamento')
def adicionar_agendamento():
    return"Agendamento ADICIONADO"

@app.route('/login')
def login():
    usuario = "Usuario 1"
    return("Você entrou",usuario)

@app.route('/logout')
def logout():

    return"Você saiu"

app.run(debug=True)     