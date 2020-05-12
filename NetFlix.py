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

x = st.slider('x')
st.write(x, 'squared is', x * x)

df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
st.dataframe(df_Movies) 

URL = df_Movies.iloc[0]["posterURL"]

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = Image.open(f)
st.image(img, caption='Sunrise by the mountains',use_column_width=True)
