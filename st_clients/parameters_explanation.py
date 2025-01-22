import streamlit as st
import requests


st.title("Parameters Explanation")

def get_explanation():
   url = "http://127.0.0.1:5000/model/explain"
   res = requests.get(url)
   return res.content

st.write(get_explanation().decode('utf-8'))
st.markdown("Original dataset credit: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho/data")