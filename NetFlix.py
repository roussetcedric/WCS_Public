import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO

st.title('Test NetFlix')

st.write("""
# My first app
Hello *world!*
""")

x = st.slider('x')
st.write(x, 'squared is', x * x)

df_Movies = pd.read_csv("https://raw.githubusercontent.com/roussetcedric/WCS/master/imdb_movies_clean_test.csv?token=AOHB6A2PJQGD37K4XBIQ4EK6YEBVM")
st.dataframe(df_Movies) 


url = df_Movies.iloc[0]["posterURL"]
response = requests.get(url)
img = Image.open(BytesIO(response.content))
st.image(img, caption='Sunrise by the mountains',use_column_width=True)
