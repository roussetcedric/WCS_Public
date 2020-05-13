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
  
#df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
df_Movies = pd.read_csv("https://drive.google.com/uc?id=10gZ-OIbxeylhxkHwxsar3D6FWj7c1qCg")
df_MovieSelected = df_Movies.iloc[0]
st.dataframe(df_Movies)
# Define Side Menu ----------------------------------------------

#Checkbox for Hospitals
st.sidebar.title("Film Filters")

ActorList_list = st.sidebar.multiselect("Select Actor", df_MovieSelected.actorsName.split(","))
DirectorList_list = st.sidebar.multiselect("Select Director", df_MovieSelected.directorsName.split(","))
GenreList_list = st.sidebar.multiselect("Select Genre", df_MovieSelected.genres.split(","))

df_Display = DisplayDataFrame(GenreList_list,DirectorList_list,ActorList_list)
st.dataframe(df_Display)

# Define the Main Page
if st.button('Validation des Parametres'):
  st.write('Validation des Parametres')
  
x = st.slider('x',1,5)
DisplayPoster(df_Display.iloc[x-1]["posterURL"])
