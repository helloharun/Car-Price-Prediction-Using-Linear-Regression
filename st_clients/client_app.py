import streamlit as st
import requests
pages = {
    "Predict Price": [
        st.Page("home.py", title="Home"),
        st.Page("sample_request.py", title="Sample Request"),
        st.Page("parameters_explanation.py", title="Parameters Explanation"),
    ],
    "About me": [
        st.Page("about_me.py", title="Contacts")
    ],
}

pg = st.navigation(pages)
pg.run()