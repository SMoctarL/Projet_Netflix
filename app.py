import streamlit as st
import pandas as pd

st.title("📺 Dashboard Netflix")

df = pd.read_csv("netflix_titles.csv")

st.subheader("Films vs Séries")
st.bar_chart(df["type"].value_counts())

st.subheader("Top pays")
st.bar_chart(df["country"].value_counts().head(10))

st.subheader("Ratings")
st.bar_chart(df["rating"].value_counts().head(10))
