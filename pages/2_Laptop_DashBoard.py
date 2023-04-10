import os
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
import plotly.express as px
import matplotlib.image as mpimg

# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path to this file's root directory
# PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(PARENT_DIR, "resources")

image = mpimg.imread(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\images\Mainimg.jpg")
st.image(image)

df = pd.read_csv(r"C:\Users\Badri Nattuva\OneDrive\Desktop\Data_Science_Intern\Laptops DashBoard\resources\data\Clean_Dataset.csv")
df.drop(labels=['Unnamed: 0', 'MRP'], axis=1, inplace=True)
st.dataframe(df)

col1, col2 ,col3 = st.columns(3)

fig_1 = px.bar(df, x='Brand', y='Price')
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.bar(df, x='Processor', y='Price')
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.scatter(df, x='Ram_1', y='Price')
col3.plotly_chart(fig_3, use_container_width=True)

st.subheader("Factors Effecting Price of Laptop")
st.caption("1. According to Brand, There will be a Price difference.")
st.caption("2. According to Processor, There will be a Price difference.")
st.caption("3. The higher RAM has a higher Price than the lower RAM.")
