import streamlit as st
import requests
import time

st.title("Car selling price prediction")


import streamlit as st

@st.dialog("Predicted Selling Price")
def show_value(value):
   st.markdown("""
   <style>
   .big-font {
      font-size:24px !important;
      font-weight: bold;
      color: #1E90FF;
   }
   .note {
      padding: 10px;
      border-radius: 5px;
      background-color: #E6F3FF;
      border-left: 5px solid #1E90FF;
   }
   </style>
   """, unsafe_allow_html=True)

   try:
      price = float(value['predicted_selling_price'])
      st.markdown(f"<p class='big-font'>$ {price:,.2f}</p>", unsafe_allow_html=True)
   except ValueError:
      st.error("The predicted selling price is not a valid number.")

   # st.markdown("<div class='note'>", unsafe_allow_html=True)
   st.warning("**Note:** This is merely a statistical prediction. Actual price may vary based on various factors.")
   st.markdown("</div>", unsafe_allow_html=True)
   
   st.markdown("---")
   
   col1, col2, col3 = st.columns([1,2,1])
   with col2:
      st.markdown("### Best wishes! 🌈")

left_column, right_column = st.columns([2,1])

with left_column:
    
   km_driven = st.number_input(
      "KM Driven",
      min_value=1,
      max_value=1000000,
      step=1,
      format="%d",         
      key="km_driven",
      placeholder="KM Driven",
      value=45000
   )

   
   l_col, m_col, r_col = st.columns(3)
   with l_col:
      fuel_type = st.radio(
         'Fuel Type',
         ("Petrol", "Diesel"))
   with m_col:
      seller_type = st.radio(
         'Seller Type',
         ("Individual", "Dealer"))
   
   with r_col:
      transmission = st.radio(
         'Transmission Type',
         ("Manual", "Automatic"))

   mileage = st.number_input(
      "Mileage",
      min_value=1,  
      max_value=100,
      step=1,       
      format="%d",  
      key="mileage",
      value=20
   )

   engine = st.number_input(
      "Engine",
      min_value=1,  
      max_value=50000,
      step=1,       
      format="%d",  
      key="engine",
      value=800
   )

   seats = st.number_input(
      "Seats",
      min_value=1,         
      max_value=10, 
      step=1,       
      format="%d",  
      key="seats",
      value=4
   )

   manufactured_year = st.number_input(
      "Manufactured Year",
      min_value=1900,
      max_value=2024,
      step=1,
      format="%d",         
      key="manufactured_year",
      value=2017
   )

   payload = {
      "km_driven": km_driven,
      "fuel": fuel_type,
      "seller_type": seller_type,
      "transmission": transmission,
      "mileage": mileage,
      "engine": engine,
      "seats": seats,
      "manufactured_year": manufactured_year
   }
   
   
   
   btn = left_column.button('Predict selling price')
   if btn:
      url = "https://raiharun.pythonanywhere.com/model/evaluate"
      res = requests.post(url=url,json=payload)
      
      # st.dialog("Predictd Selling Price", res.json(), width="small")
      # st.write(f"Payload: {res.json()}")

      # with st.expander("Predicted Selling Price"):
      #    st.write(res.json())
      show_value(res.json())
