import pandas as pd




df = pd.read_excel('movie_metadata.xlsx')
df['genero'] = df['genres'].str.replace('|', ' ')
df['movie_title'] = df['movie_title'].str.replace('Â', 'a')
df['plot_keywords'] = df['plot_keywords'].str.replace('|', ' ')
df['texto'] = df[['genero', 'plot_keywords']].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
row = df[['genero', 'plot_keywords', 'texto']].iloc[0]
print(df['movie_title'])
#print(row)
#print(df['texto'].iloc[0])

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

tfidf = TfidfVectorizer(max_features=2000)

X = tfidf.fit_transform(df['texto'])

peliculas = pd.Series(df.index, index=df['movie_title'])
peliculas.index = peliculas.index.str.strip()

buscar = input('pelicula:')
if buscar != "":
        indice = peliculas[buscar]
        consulta = X[indice]
        consulta.toarray()
        similitud = cosine_similarity(consulta, X)
        similitud = similitud.flatten()

        import matplotlib.pyplot as plt
        plt.plot(similitud)
        (-similitud).argsort()
        plt.plot(similitud[(-similitud).argsort()])
        recomendacion = (-similitud).argsort()[1:11]
        resul = df['movie_title'].iloc[recomendacion]
        print(resul)
else:
    print('la pelicula " " no existe')