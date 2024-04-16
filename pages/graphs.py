import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title('3D Plot Visualization')

st.write("This is a 3D plot visualization using Women's Clothing E-Commerce Reviews dataset that revolves around the reviews written by customers")

df = pd.read_csv('WomensClothingE-CommerceReviews.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(1,6):
    ax.scatter(df[df['Rating']==i]['Age'], df[df['Rating']==i]['Rating'], df[df['Rating']==i]['Positive Feedback Count'], label = 'Rating '+str(i))
ax.set_xlabel('Age')
ax.set_ylabel('Rating')
ax.set_zlabel('Positive Feedback Count')
plt.legend()

st.pyplot(fig)


st.write('The 3D plot visualization shows the distribution of Age, Rating and Positive Feedback Count. It can be observed that the distribution of Rating 5 is more compared to other ratings. The distribution of Rating 2 is the least. The distribution of Age is more between 30 to 50. The distribution of Positive Feedback Count is more between 0 to 20.')