import streamlit as st
import pandas as pd
from PIL import Image
import urllib.request
import io

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
    MOVIEDB_API_KEY = '076f7a313a578e7764aa7344b143bc30'
    poster_base_url = 'https://image.tmdb.org/t/p/original'
    movie_url = 'https://api.themoviedb.org/3/find/'+id+'?api_key='+MOVIEDB_API_KEY+'&language=fr-FR&external_source=imdb_id'
    try:
      with urllib.request.urlopen(movie_url) as response:
        data = json.loads(response.read())
        urls_array = poster_base_url+data['movie_results'][0]['poster_path']
    except:
       urls_array = ""
    st.write(urls_array)
    return urls_array

import time
my_bar = st.progress(0)
for percent_complete in range(10):
  time.sleep(0.1)
  my_bar.progress(percent_complete + 10)
#df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
df_Movies = pd.read_csv("https://drive.google.com/uc?id=10gZ-OIbxeylhxkHwxsar3D6FWj7c1qCg")
#Select Movie
title = st.text_input('Movie title', 'Type your film here !')
st.write('The current movie title is', title)
df_MovieSelected = df_Movies[df_Movies["primaryTitle"].str.contains(title)]
st.dataframe(df_MovieSelected["primaryTitle"])
MovieSelectedTitle = st.selectbox('Choose your film ?', df_MovieSelected["primaryTitle"].tolist())
st.write('You selected:', MovieSelectedTitle)
df_MovieSelectedOne = df_Movies[df_Movies["primaryTitle"] == MovieSelectedTitle]
st.dataframe(df_MovieSelectedOne)

# Define Side Menu ----------------------------------------------
st.sidebar.title("Film Filters")
ActorList_list = st.sidebar.multiselect("Select Actor", df_MovieSelectedOne.actorsName.split(","))
DirectorList_list = st.sidebar.multiselect("Select Director", df_MovieSelectedOne.directorsName.split(","))
GenreList_list = st.sidebar.multiselect("Select Genre", df_MovieSelectedOne.genres.split(","))

df_Display = DisplayDataFrame(GenreList_list,DirectorList_list,ActorList_list)
st.dataframe(df_Display)

# Define the Main Page
if st.button('Validation des Parametres'):
  st.write('Validation des Parametres')
  
x = st.slider('x',1,5)
DisplayPoster(get_poster_from_api(df_Display.iloc[x-1]["tconst"]))
