from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos Anéis - a Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'A revolução dos bichos',
        'autor': 'George Orwell'
    },
    {
        'id': 3,
        'titulo': 'Frankenstein',
        'autor': 'Mary Shelley' 
    },
]

#Consultar (todos os livros)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)  #toda a API usa o formato JSON para retornar os arquivos

#Consultar usando ID
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:       #procurando a propriedade id em todo o dicionario de livros
            return jsonify(livro)    

#Editar um livro por id
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar 
@app.route('/livros', methods=['POST'])
def criar_livro ():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

#Defininindo uma rota para aplicação rodar
app.run(port=5000,host='localhost',debug=True)