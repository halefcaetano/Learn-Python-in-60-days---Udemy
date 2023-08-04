import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore 
         et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip 
         ex ea commodo consequat.""")
st.subheader("Our team")


col1, col2, col3 = st.columns(3)

df = pandas.read_csv("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app3/data1.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app3/images/" + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app3/images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days---Udemy/apps/app3/images/" + row["image"])