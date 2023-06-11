# 1 objetivo - Criar uma api de disponibiliza a consulta, criaçao, ediçao e exclusao
# 2 url base - localhost
# 3 Endpoints - 
   #localhost/livros (GET)
   #localhost/livros/id (POST)
   #localhost/livros/id (PUT)
   #localhost/livos/id (DELETE)

# 4 quais recursos - Livros
from flask import Flask, jsonify, request


app = Flask(__name__)


anuncios = [
    {
        'id': 1,
        'anuncio': 'Sou Pedro Silva, tenho 28 anos e sou de SP. Influenciador apaixonado por aventuras radicais, viagens e adrenalina. Minha audiência adora acompanhar minhas experiências...'
    },
    {
       'id': 2,
       'anuncio': 'Sou Isabella Rodrigues, tenho 25 anos e sou do RJ, uma influenciadora gastronômica com um paladar refinado e adoro compartilhar minhas descobertas culinárias com meus seguidores. Minha...'
    },
    {
       'id': 3,
       'anuncio': 'Sou Sofia Santos, tenho 24 anos e sou de MG, uma influenciadora de moda e estilo de vida, sempre em busca das últimas tendências e inspirando meus seguidores com dicas de moda e estilo. Minha audiência é...'
    },

    {
       'id': 4,
       'anuncio': 'Sou John Anderson, tenho 21 anos e sou de GO, um influenciador de tecnologia sempre atualizado sobre os últimos gadgets e tendências tecnológicas. Minha audiência é formada por entusiastas da tecnologia...'
    },
    
    ]

# Consultar(todos)
@app.route('/anuncios', methods=['GET'])
def obter_anuncios():
    return jsonify(anuncios)

# Consulta(id)
@app.route('/anuncios/<int:id>', methods=['GET'])
def obter_anuncios_por_id(id):
    for ads in anuncios:
        if ads.get('id') == id:
            return jsonify(ads)

# Editar
@app.route('/anuncios/<int:id>', methods=['PUT'])
def editar_anuncios_por_id(id):
    anuncio_alterado = request.get_json()
    for indice, ads in enumerate(anuncios):
        if ads.get('id') == id:
            anuncios[indice].update(anuncio_alterado)
            return jsonify(anuncios[indice])

#criar 
@app.route('/anuncios', methods=['POST'])
def incluir_novo_anuncios():
    novo_anuncio = request.get_json()
    anuncios.append(novo_anuncio)

    return jsonify(anuncios)

# Excluir
@app.route('/anuncios/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, ads in enumerate(anuncios):
        if ads.get('id') == id:
            del anuncios[indice]
    return jsonify(anuncios)



#iniciar

if __name__ == '__main__':
    import os

    host = '0.0.0.0'
    port  = int(os.environ.get("PORT", 5000))

    app.run(host, port)
