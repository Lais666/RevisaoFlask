from flask import Flask, render_template

app = Flask(__name__)

# Lista de livros fictícios
livros = [
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945},
]

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)
