import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances


df = pd.read_excel('movie_metadata.xlsx')

df['genero'] = df['genres'].str.replace('|', ' ')
df['movie_title'] = df['movie_title'].str.strip().str.replace('Â', '').str.strip()
df['plot_keywords'] = df['plot_keywords'].str.replace('|', ' ')
df['texto'] = df[['genero', 'plot_keywords']].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

row = df[['genero', 'plot_keywords', 'texto']].iloc[0]
print(df['movie_title'])

#print(row)
#print(df['texto'].iloc[0])
print(df['movie_title'].unique())


tfidf = TfidfVectorizer(max_features=2000)
X = tfidf.fit_transform(df['texto'])

peliculas = pd.Series(df.index, index=df['movie_title'].str.strip())

# peliculas.index = peliculas.index.str.strip()

# buscar = input('pelicula:')
# if buscar != "":
#         indice = peliculas[buscar]
#         consulta = X[indice]
#         consulta.toarray()
#         similitud = cosine_similarity(consulta, X)
#         similitud = similitud.flatten()

#         import matplotlib.pyplot as plt
#         plt.plot(similitud)
#         (-similitud).argsort()
#         plt.plot(similitud[(-similitud).argsort()])
#         recomendacion = (-similitud).argsort()[1:11]
#         resul = df['movie_title'].iloc[recomendacion]
#         print(resul)
# else:
#     print('la pelicula " " no existe')



"""
Esta función `movie_recommended` toma el título de una película como entrada, limpia y normaliza el texto eliminando espacios adicionales y caracteres no deseados. 
Luego, busca si el título de la película se encuentra en el índice de títulos de películas. 
Si la película está en el índice, se obtiene el índice correspondiente y se calcula la similitud de coseno entre la película consultada y todas las demás películas en el conjunto de datos. 
Se generan recomendaciones basadas en los índices de mayor similitud, excluyendo la película consultada, y se devuelven los títulos de las películas recomendadas. 
Si la película no está en el índice, se imprime un mensaje de error y se devuelve una lista indicando que la película no existe en la base de datos.
"""

def movie_recommended(pelicula):
        pelicula = pelicula.strip()
        pelicula = pelicula.replace('Â', '') 
        print(f"Buscando: {pelicula}")  # Depuración

        if pelicula in peliculas.index:
                indice = peliculas[pelicula]
                consulta = X[indice]
                similitud = cosine_similarity(consulta, X).flatten()
                recomendacion_indices = (-similitud).argsort()[1:10]
                return df['movie_title'].iloc[recomendacion_indices].tolist()
        else:
                print(f"La película '{pelicula}' no está en el índice")  # Depuración
                return ['La pelicula no existe en la base de datos.']
