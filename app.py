import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Carrega as descrições do arquivo JSON
with open('descriptions.json', 'r', encoding='utf-8') as f:
    descriptions = json.load(f)

# Diretórios de imagens
input_dir = 'static/images'

# Lista de imagens
images = sorted([img for img in os.listdir(input_dir) if img.startswith('imagem')])

current_index = 0
ratings = []


@app.route('/')
def index():
    global current_index
    if current_index >= len(images):
        return redirect(url_for('finalizacao'))

    image = images[current_index]
    return render_template('index.html', image=image, index=current_index + 1)


@app.route('/visualizar_resposta', methods=['POST'])
def visualizar_resposta():
    global current_index
    image = images[current_index]
    description = descriptions.get(image.split('.')[0], "Descrição não disponível.")

    return render_template('resposta.html', image=image, description=description, index=current_index + 1)


@app.route('/classificar', methods=['POST'])
def classificar():
    global current_index, ratings
    rating = int(request.form['rating'])
    ratings.append(rating)

    current_index += 1
    return redirect(url_for('index'))


@app.route('/finalizacao')
def finalizacao():
    media = sum(ratings) / len(ratings) if ratings else 0
    return render_template('finalizacao.html', media=media)

@app.route('/avaliar_projeto', methods=['POST'])
def avaliar_projeto():
    # Redireciona para a página do GitHub ou outro destino.
    return redirect("https://github.com/Wellington-Barbosa/Image-Specialist")  # Substitua pela URL do seu projeto no GitHub


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
