import pickle
import pandas as pd
import requests

# Loading Pickle Files
with open('movies.pkl','rb') as f:
    df = pickle.load(f)
with open('similarity.pkl','rb') as f:
    similarity = pickle.load(f)

# List of all movies_name
movie_name = df['title'].unique().tolist()

# Fetch poster from api
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return f'http://image.tmdb.org/t/p/w500/{data["poster_path"]}'

# Method used for recommending movies
def recommend_movies(movie_name):
    movie_index = df[df['title'] == movie_name].index[0]
    similarity_score = similarity[movie_index]
    similar_movies_list = sorted(list(enumerate(similarity_score)), reverse=True, key=lambda x:x[1])[1:6]
        
    recommended_movies_name = []
    recommend_movies_poster = []
    
    for i in similar_movies_list:
        recommended_movies_name.append(df.iloc[i[0],:].title)
        # Fetch poster from api
        movie_id = df.iloc[i[0],:].movie_id
        recommend_movies_poster.append(fetch_poster(movie_id))

    # Creating list of tuples of recommended movies name like [('name1','name2','name3','name4','name5','name6')]
    it = iter(recommended_movies_name)
    recommended_movies_name = list(zip(it, it, it, it, it))
    it1 = iter(recommend_movies_poster)
    recommend_movies_poster = list(zip(it1, it1, it1, it1, it1))
        
    return recommended_movies_name, recommend_movies_poster
