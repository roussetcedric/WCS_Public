import streamlit as st
import pandas as pd
st.write("""
# My first app
Hello *world!*
""")

x = st.slider('x')
st.write(x, 'squared is', x * x)
