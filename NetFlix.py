import streamlit as st
import pandas as pd
from PIL import Image
import urllib.request
import io

df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
st.dataframe(df_Movies) 

def DisplayPoster(UrlToDisplay) :
  if UrlToDisplay :
    with urllib.request.urlopen(UrlToDisplay) as url:
      f = io.BytesIO(url.read())
    img = Image.open(f)
    st.image(img, caption=df_Movies.iloc[x-1]["primaryTitle"],width=150)

# Define Side Menu ----------------------------------------------
st.sidebar.title("Film Survey :movie:")
movie = st.sidebar.multiselect("Which do you like the most?",
                                ("Vanilla Yogurt","Berry Yogurt","Greek Yogurt"))

# Define the Main Page
Titre = "Voici la sélection de film basé sur"
Param = ""
st.title(Titre + Param)

x = st.slider('x',1,5)
DisplayPoster(df_Movies.iloc[x-1]["posterURL"])

if st.button('Titre'):
  Param = df_Movies.iloc[x-1]["primaryTitle"]
  st.write(df_Movies.iloc[x-1]["primaryTitle"])
  st.title(Titre + Param)
if st.button('Genre'):
  Param = df_Movies.iloc[x-1]["genres"]
  st.write(df_Movies.iloc[x-1]["genres"])
  st.title(Titre + Param)
if st.button('Director'):
  Param = df_Movies.iloc[x-1]["directorsName"]
  st.write(df_Movies.iloc[x-1]["directorsName"])
  st.title(Titre + Param)
