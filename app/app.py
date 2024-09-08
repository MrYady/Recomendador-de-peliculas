"""
Este script define una aplicación web usando Flask que permite a los usuarios buscar recomendaciones de películas. 
La aplicación tiene una única ruta (`/`) que maneja tanto solicitudes GET como POST. 
Cuando se accede a la ruta mediante un método GET, se renderiza un formulario HTML. 
Cuando se envía el formulario mediante un método POST, el título de la película ingresado se utiliza para buscar recomendaciones utilizando la función `movie_recommended` importada. 
Las recomendaciones, junto con el formulario, se pasan de vuelta a la plantilla `index.html` para su visualización. 
"""

from flask import Flask, render_template, request
import forms
from movie_recomiendo import movie_recommended

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.CommentForm(request.form)
    recomendation = []
    
    if request.method == 'POST':
        if form.validate():
            search = form.peli.data
            print(f"Buscando la película: {search}")  # Depuración
            recomendation = movie_recommended(search)
            print(f"Recomendaciones: {recomendation}")  # Depuración
        else:
            print("El formulario no es válido.")  # Depuración
        
    return render_template('index.html', form=form, recomendacion=recomendation)


if __name__ == '__main__':
    app.run(debug=True)
