from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Diretórios de imagens e respostas
input_dir = 'input'
output_dir = 'output'

# Lista de imagens
images = sorted([img for img in os.listdir(input_dir) if img.startswith('imagem')])
responses = sorted([resp for resp in os.listdir(output_dir) if resp.startswith('resposta')])

# Variáveis globais
current_index = 0
ratings = []


@app.route('/')
def index():
    global current_index
    if current_index >= len(images):
        # Redireciona para a página de conclusão quando todas as imagens forem classificadas
        return redirect(url_for('finalizacao'))

    image = images[current_index]
    return render_template('index.html', image=image, index=current_index + 1)


@app.route('/visualizar_resposta', methods=['POST'])
def visualizar_resposta():
    global current_index
    image = images[current_index]
    response_file = responses[current_index]

    with open(os.path.join(output_dir, response_file), 'r') as file:
        response_text = file.read()

    return render_template('resposta.html', image=image, response=response_text, index=current_index + 1)


@app.route('/classificar', methods=['POST'])
def classificar():
    global current_index, ratings
    rating = int(request.form['rating'])
    ratings.append(rating)

    current_index += 1
    return redirect(url_for('index'))


@app.route('/finalizacao')
def finalizacao():
    # Calcula a média das avaliações
    media = sum(ratings) / len(ratings) if ratings else 0

