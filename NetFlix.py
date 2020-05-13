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
 
df_Display = pd.DataFrame()
def DisplayDataFrame(GenreList,DirectorList,ActorList):
  st.write("DisplayDataFrameModule")
  st.write(ActorList)
  st.write(DirectorList)
  st.write(GenreList)
  df_Display = df_Movies[df_Movies["genres"].isin(GenreList)]
  st.dataframe(df_Display)
  
df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
df_MovieSelected = df_Movies.iloc[0]

# Define Side Menu ----------------------------------------------

#Checkbox for Hospitals
st.sidebar.title("Film Filters")

ActorList_list = st.sidebar.multiselect("Select Actor", df_MovieSelected.actorsName.split(","))
DirectorList_list = st.sidebar.multiselect("Select Actor", df_MovieSelected.directorsName.split(","))
GenreList_list = st.sidebar.multiselect("Select Actor", df_MovieSelected.genres.split(","))

# Define the Main Page

DisplayDataFrame(GenreList_list,DirectorList_list,ActorList_list)
                         
x = st.slider('x',1,df_Display.shape[0])
DisplayPoster(df_Display.iloc[x-1]["posterURL"])

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
