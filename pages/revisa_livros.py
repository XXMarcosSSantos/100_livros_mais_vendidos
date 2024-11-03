import streamlit as st 
import pandas as pd


st.set_page_config(layout="wide")


df_revisa = pd.read_csv('customer reviews.csv')
df_top_100livros = pd.read_csv('Top-100 Trending Books.csv')

livros = df_top_100livros["book title"].unique()
livro = st.sidebar.selectbox("books", livros)

df_livros = df_top_100livros[df_top_100livros["book title"] == livro]
df_revisa_f = df_revisa[df_revisa["book name"] == livro]

book_title = df_livros["book title"].iloc[0]
book_genre = df_livros["genre"].iloc[0]
book_price = f"${df_livros['book price'].iloc[0]}"
book_rating = df_livros["rating"].iloc[0]
book_year = df_livros["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("price", book_price)
col2.metric("rating", book_rating)
col3.metric("year of publication", book_year)

st.divider()

for row in df_revisa_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])
