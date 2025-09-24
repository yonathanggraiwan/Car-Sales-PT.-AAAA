import streamlit as st
import predict, home

st.set_page_config(page_title = "Car Market Price Prediction",
                   layout = 'centered',
                   initial_sidebar_state = 'expanded')
with st.sidebar:
    st.write('# Navigation Sidebar')
    navigation = st.radio('Page', ['Home', 
                                #    'Exploratory Data Analysis (EDA) Section', 
                                   'Car Market Price Prediction Section'])

# if navigation == 'Exploratory Data Analysis (EDA) Section':
#     eda.run()

if navigation == 'Car Market Price Prediction Section':
    predict.run()

if navigation == 'Home':
    home.run()
    
else:
    home.run()