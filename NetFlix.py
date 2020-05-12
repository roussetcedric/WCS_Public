import streamlit as st
import pandas as pd
from PIL import Image
import urllib.request
import io

df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
df_Display = []
Param = "Initilialisation"

def DisplayPoster(UrlToDisplay) :
  if UrlToDisplay :
    with urllib.request.urlopen(UrlToDisplay) as url:
      f = io.BytesIO(url.read())
    img = Image.open(f)
    st.image(img,width=400)

# Define Side Menu ----------------------------------------------
st.sidebar.title("Film Survey :happy:")
Choix = st.sidebar.multiselect("Which do you like the most?",
                                ("Genre","Director","Acteurs"))

# Define the Main Page
st.write("Voici la sélection de film basée sur")
st.write(Choix)
st.write(Param)

if st.button('Titre'):
  Param = df_Movies.iloc[x-1]["primaryTitle"]
  st.write(df_Movies.iloc[x-1]["primaryTitle"])
  df_Display = df_Movies.sort_values(by=['primaryTitle'])[0:5]
if st.button('Genre'):
  Param = df_Movies.iloc[x-1]["genres"]
  st.write(df_Movies.iloc[x-1]["genres"])
  df_Display = df_Movies.sort_values(by=['genres'])[0:5]
if st.button('Director'):
  Param = df_Movies.iloc[x-1]["directorsName"]
  st.write(df_Movies.iloc[x-1]["directorsName"])
  df_Display = df_Movies.sort_values(by=['directorsName'])[0:5]
  
st.dataframe(df_Display)

x = st.slider('x',1,5)
DisplayPoster(df_Display.iloc[x-1]["posterURL"])
