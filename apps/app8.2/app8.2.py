import glob
import streamlit as st
import plotly.express as px

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("/Users/halefcaetano/Desktop/python/Learn-Python-in-60-days"
                             "---Udemy/apps/app8.2/diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])


dates = [21, 22, 23, 24, 25, 26, 27]

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)


dates = [21, 22, 23, 24, 25, 26, 27]
st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)
