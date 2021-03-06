import pandas as pd
import numpy as np

# Movies without rating

movies = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/movies.csv')
movies.columns = ['Movie_ID', 'Title', 'Genre']

movie_rating = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/movielens-data/master/ratings.csv')
movie_rating.columns = ['User_ID', 'Movie_ID', 'Rating', 'Moment']

mean_rating_by_movie = movie_rating.groupby('Movie_ID')['Rating'].mean()

mean_movies = movies.join(mean_rating_by_movie, on='Movie_ID')

movies_no_rating = mean_movies['Rating'].isnull()
mean_movies[movies_no_rating].replace(np.NAN, 0)
