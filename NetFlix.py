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
    
def DisplayDataFrame(Option):
  st.write(Option)
  #if Option != [] :
    #df_DisplayTest = df_Movies.sort_values(by=Option)[0:5]
  st.dataframe(df_Movies[0:5])
  
df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
df_Display = pd.DataFrame()
df_MovieSelected = df_Movies.iloc[0]

# Define Side Menu ----------------------------------------------

#Checkbox for Hospitals
st.sidebar.title("Film Filters")
st.write(df_MovieSelected.actorsName.split(","))
st.write(df_MovieSelected.directorsName.split(","))

ActorList_list = st.sidebar.selectbox("Select Actor", df_MovieSelected.actorsName.split(","))
DirectorList_list = st.sidebar.selectbox("Select Actor", df_MovieSelected.directorsName.split(","))

Choix = st.sidebar.multiselect("Which do you like the most?",
                                ("Genre","Director","Acteurs"))

# Define the Main Page
st.write("Voici la sélection de film basée sur les paramètres :")
st.write(Choix)

DisplayDataFrame(Choix)

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
