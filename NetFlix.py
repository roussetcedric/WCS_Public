import streamlit as st
import pandas as pd
from PIL import Image
import urllib.request
import io

st.title('Test NetFlix')
st.write("""
# My first app
Hello *world!*
""")

# Define Side Menu ----------------------------------------------
st.sidebar.title("Film Survey :movie:")
movie = st.sidebar.multiselect("Which do you like the most?",
                                ("Vanilla Yogurt","Berry Yogurt","Greek Yogurt"))

x = st.slider('x',1,5)

df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
st.dataframe(df_Movies) 

URL = df_Movies.iloc[x-1]["posterURL"]

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = Image.open(f)
st.image(img, caption='Sunrise by the mountains',use_column_width=True)

if st.button('Titre'):
  st.write(df_Movies.iloc[x-1]["primaryTitle"])
if st.button('Genre'):
  st.write(df_Movies.iloc[x-1]["genres"])
if st.button('Director'):
  st.write(df_Movies.iloc[x-1]["directorNames"])
