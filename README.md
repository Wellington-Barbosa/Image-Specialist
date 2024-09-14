# Projeto de Inteligência Artificial Generativa - Avaliação de Imagens

Este projeto foi desenvolvido como parte de um curso de Inteligência Artificial Generativa, com o objetivo de criar uma aplicação web que permite a análise de imagens por uma IA e a avaliação das respostas geradas.

## Estrutura do Projeto

O projeto está organizado em duas pastas principais:

- **input/**: Contém as imagens que serão analisadas pela IA.
- **output/**: Contém as respostas geradas pela IA para cada imagem.

## Funcionalidades

- Exibição sequencial de 11 imagens.
- Para cada imagem, o usuário pode visualizar a resposta gerada pela IA.
- O usuário pode avaliar a resposta da IA usando uma classificação de 1 a 5 estrelas.
- Após a classificação de uma imagem, a próxima é exibida até que todas as imagens sejam avaliadas.
- Após a classificação da última imagem, o usuário é redirecionado para uma página que exibe a média de todas as avaliações.
- Um botão na página final permite que o usuário avalie o projeto no GitHub.

## Execução do Projeto

### 1. Configuração do Ambiente Virtual

1. Crie o ambiente virtual:
   ```bash
   python -m venv venv

### 2. Ative o ambiente virtual:

- **No Windows:**
    ```bash
    venv\Scripts\activate

- **No macOS/Linux:**
    ```bash
    source venv/bin/activate

### 3. Instale as dependências:

    pip install -r requirements.txt

### 4. Execute o projeto:
    
    python app.py

### 5. Acesse o aplicativo no navegador através de http://127.0.0.1:5000.

## Como Usar:

1. O projeto exibirá uma imagem da pasta input/.
2. Clique no botão "Visualizar Resposta da IA" para ver a resposta gerada pela IA.
3. Avalie a resposta da IA com uma classificação de 1 a 5 estrelas.
4. Após a avaliação, a próxima imagem será exibida.
5. Repita o processo até que todas as 11 imagens sejam classificadas.
6. Após a última imagem, você será redirecionado para uma página que exibirá a média das avaliações e um botão "Avaliar o Projeto" que levará você para a página do projeto no GitHub.
    
## Melhorias na Interface

- O layout foi otimizado para se adaptar a diferentes tamanhos de tela, proporcionando uma experiência agradável tanto em desktops quanto em dispositivos móveis.
- As páginas são organizadas de forma intuitiva, com botões e inputs responsivos e de fácil utilização.

## Exemplo de Uso

![Imagem_01](https://github.com/Wellington-Barbosa/Image-Specialist/raw/main/input/imagem_01.png)

- **Resposta da IA:**
	```bash
	Descrição: Esta é uma imagem de um cachorro da raça Golden Retriever correndo em um gramado.
    
## Insights

Durante o desenvolvimento deste projeto, foi possível entender como integrar uma IA para análise de imagens com uma interface web. Algumas das lições aprendidas incluem:
    
- Manipulação de arquivos de imagens e texto com Python.
- Criação de interfaces dinâmicas com Flask.
- A importância de validar as respostas da IA para garantir que a análise seja consistente com as expectativas dos usuários.

## Possibilidadees Futuras

- Adicionar suporte a IA em tempo real para análise de novas imagens.
- Melhorar o sistema de avaliação e permitir que as avaliações sejam armazenadas em um banco de dados para análise posterior.


