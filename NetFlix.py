import streamlit as st
import pandas as pd
from PIL import Image
import io
import json
import requests
import urllib.request
from bs4 import BeautifulSoup
import time

# Load Data -----------------------------------------------------
# df_Movies = pd.read_csv("https://drive.google.com/uc?id=10gZ-OIbxeylhxkHwxsar3D6FWj7c1qCg")
df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS_Public/master/imdb_movies_light.csv")

# Define Function --------------------------------------------
def DisplayPoster(UrlToDisplay) :
  if UrlToDisplay :
    with urllib.request.urlopen(UrlToDisplay) as url:
      f = io.BytesIO(url.read())
    img = Image.open(f)
    st.image(img,width=400)
 
#df_Display = pd.DataFrame()
def DisplayDataFrame(GenreList,DirectorList,ActorList):
  st.write("DisplayDataFrameModule")
  st.write(ActorList)
  df_DisplayLocal = df_Movies[df_Movies["actorsName"].str.contains('|'.join(ActorList))]
  st.write(DirectorList)
  df_DisplayLocal = df_DisplayLocal[df_DisplayLocal["directorsName"].str.contains('|'.join(DirectorList))]
  st.write(GenreList)
  df_DisplayLocal = df_DisplayLocal[df_DisplayLocal["genres"].str.contains('|'.join(GenreList))]
  return df_DisplayLocal

def get_poster_from_api(movie_id):
    st.write("movie_id : ", movie_id)
    MOVIEDB_API_KEY = '076f7a313a578e7764aa7344b143bc30'
    poster_base_url = 'https://image.tmdb.org/t/p/original'
    poster_url = ''
    movie_url = 'https://api.themoviedb.org/3/find/'+movie_id+'?api_key='+MOVIEDB_API_KEY+'&language=fr-FR&external_source=imdb_id'
    try:
        with urllib.request.urlopen(movie_url) as response:
            data = json.loads(response.read())
        poster_url = poster_base_url+data['movie_results'][0]['poster_path']
    except:
        poster_url = "https://raw.githubusercontent.com/roussetcedric/WCS_Public/master/pngtree-latest-movie-poster-design-image_163485.jpg"
    return poster_url
  
# Define Main Programm

my_bar = st.progress(0)
for percent_complete in range(100):
  time.sleep(0.01)
  my_bar.progress(percent_complete + 1)

#Select Movie
title = st.text_input('Choose your film', 'Type your film here !')
df_MovieSelected = df_Movies[df_Movies["primaryTitle"].str.contains(title)]
st.dataframe(df_MovieSelected["primaryTitle"])
MovieSelectedTitle = st.selectbox('Choose your film ?', df_MovieSelected["primaryTitle"].tolist())
df_MovieSelectedOne = df_Movies[df_Movies["primaryTitle"] == MovieSelectedTitle]
st.dataframe(df_MovieSelectedOne)
st.write(df_MovieSelectedOne["tconst"])
DisplayPoster(get_poster_from_api(df_MovieSelectedOne["tconst"]))

# Define Side Menu ----------------------------------------------
st.sidebar.title("Film Filters")
ActorList_list = st.sidebar.multiselect("Select Actor", df_MovieSelectedOne.actorsName)
DirectorList_list = st.sidebar.multiselect("Select Director", df_MovieSelectedOne.directorsName)
GenreList_list = st.sidebar.multiselect("Select Genre", df_MovieSelectedOne.genres)

df_Display = DisplayDataFrame(GenreList_list,DirectorList_list,ActorList_list)
st.dataframe(df_Display)
  
x = st.slider('x',1,5)
DisplayPoster(get_poster_from_api(df_Display.iloc[x-1]["tconst"]))
