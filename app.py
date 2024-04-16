
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_pages import Page, show_pages

st.title('Women’s Clothing E-Commerce Analysis')

show_pages([
    Page("app.py", "Home", "🏠"),
    Page("pages/graphs.py", "3D Plot Visualization", "📈"),
    Page("pages/imgprocess.py", "Image Procesing", "📷"),
    Page("pages/textvis.py", "Text Visualization", "📜")
])
st.sidebar.image("https://i.imgur.com/9TX68Ou.gif")
st.sidebar.markdown("Created with ❤️ by Rajasree Baruri")

st.write('This is a Women’s Clothing E-Commerce Analysis using dataset that revolves around the reviews written by customers. ')

st.write('Here is a DataFrame.')


df = pd.read_csv('WomensClothingE-CommerceReviews.csv')
st.write(df.head(10))


st.write('The dataset contains 23486 rows and 10 columns.')





