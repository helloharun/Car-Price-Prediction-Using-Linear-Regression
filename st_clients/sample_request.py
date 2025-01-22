import streamlit as st
import requests
import json
import clipboard

st.title("Sample Request")

def get_sample_request():
   url = "http://127.0.0.1:5000/model/sample"
   res = requests.get(url)
   decoded_response = res.content.decode('utf-8')
   return decoded_response

def on_copy_click(text):
    # st.session_state.copied.append(text)
    clipboard.copy(text)
   
l_col, r_col = st.columns(2)
with r_col:
   st.button("📋", on_click=on_copy_click(get_sample_request()))

with l_col:
   st.write(json.loads(get_sample_request()))