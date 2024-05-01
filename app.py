from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    with open('peliculas.json', 'r', encoding='utf-8') as fich:
        datos = json.load(fich)

    search_term = request.form.get('search_term', '')
    selected_genre = request.form.get('selected_genre', '')
    resultados = []

    if search_term and selected_genre:
        for pelicula in datos:
            if search_term.lower() in peliculas['title'].lower() and selected_genre.lower() in peliculas.get('genre', '').lower():
                resultados.append(peliculas)
    elif search_term:
        for pelicula in datos:
            if search_term.lower() in peliculas['title'].lower():
                resultados.append(peliculas)
    elif selected_genre:
        for pelicula in datos:
            if selected_genre.lower() in peliculas.get('genre', '').lower():
                resultados.append(pelicula)
    else:
        resultados = datos

    generos_unicos = set(pelicula.get('genre', '') for pelicula in datos)

    return render_template('contact.html', resultados=resultados, search_term=search_term, selected_genre=selected_genre, generos_unicos=generos_unicos)

@app.route('/pelicula/<int:id>')
def mostrar_pelicula(id):
    with open('peliculas.json', 'r', encoding='utf-8') as fich:
        datos = json.load(fich)

    pelicula_encontrada = None
    for pelicula in datos:
        if pelicula.get('id') == id:
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada:
        return render_template('pelicula.html', pelicula=pelicula_encontrada)
    else:
        return render_template('article.html', message='Película no encontrada'), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port, debug=True)

