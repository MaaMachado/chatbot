from flask import Flask, request, jsonify
import random
from nltk.tokenize import word_tokenize
import nltk

# nltk.download('punkt')

#Pares de Perguntas e respostas
perguntas_respostas = {
    1: "Como posso ajudar você neste belo dia?",
    2: "Estou bem, obrigada por perguntar. Espero que você também esteja bem.",
    3: "Meu nome é ChatBot. Sou um serviço de contato criado para introduzir os estudo de Inteligência Artificial.",
    4: "Posso responder a perguntar simples para iniciar um contato com o usuário.",
    5: "Tchau! Muito obrigada por testar esse serviço! Tenha um bom dia!"
}

cumprimento  = ["olá", "oi", "ai", "ola", "hey", "ei"]
gentileza = ["tudo bem", "como vai", "tudo certo", "bem"]
nome = ["qual é o seu nome", "como você se chama", "seu nome", "nome"]
funcao = ["função", "o que você pode fazer", "quais são suas habilidades", "funções", "o que você faz", "funcao", "qual é a sua função"]
despedida = ["adeus", "Bye", "até logo", "tchau"]

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_question = data['question']
    resposta = responder_pergunta(user_question)
    print(resposta)
    return jsonify({'response': resposta})

def responder_pergunta(pergunta):

    tokens = word_tokenize(pergunta.lower())

    if len(tokens) > 0:
        for token in tokens:
            if token in cumprimento:
                return perguntas_respostas.get(1)
            
            elif token in gentileza:
                return perguntas_respostas.get(2)
            
            elif token in nome:
                return perguntas_respostas.get(3)
            
            elif token in funcao:
                return perguntas_respostas.get(4)
            
            elif token in despedida:
                return perguntas_respostas.get(5)
    
    return "Desculpe, não entendi a pergunta."
           

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)