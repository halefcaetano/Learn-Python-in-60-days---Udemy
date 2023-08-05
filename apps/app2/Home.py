import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app2/images/photo.png")

with col2:
    st.title("Ardit Sulce")
    st.info("My professor")


st.write("Just some text bellow the picture.")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app2/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app2/images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app2/images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
