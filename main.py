import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_revisa = pd.read_csv('customer reviews.csv')
df_top_100livros = pd.read_csv('Top-100 Trending Books.csv')

preco_max = df_top_100livros["book price"].max()
preco_min = df_top_100livros["book price"].min()

max_preco = st.sidebar.slider("price range", preco_min, preco_max, preco_max)
df_livros = df_top_100livros[df_top_100livros["book price"] <= max_preco]

fig = px.bar(df_livros["year of publication"].value_counts())
fig2 = px.histogram(df_livros["book price"])
df_livros

col1 , col2 = st.columns(2) 
col1.plotly_chart(fig)
col2.plotly_chart(fig2)