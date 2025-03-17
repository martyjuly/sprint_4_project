# Code in app.py provided by AI/Dot. 

import streamlit as st
import pandas as pd
import plotly.express as px

file_path = 'vehicles_us.csv'
df = pd.read_csv(file_path)

st.header('Car Dataset') 

fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

fig_scatter = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
st.plotly_chart(fig_scatter)

if st.checkbox('Show only automatic transmission'):
    df_filtered = df[df['transmission'] == 'automatic']
    st.plotly_chart(px.histogram(df_filtered, x='price', title='Price Distribution (Automatic Only)'))
