import streamlit as st
import datetime
from streamlit_lottie import st_lottie
import json
import numpy as numpy
import requests

###Lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

Galley_Url = "https://lottie.host/0c56d477-6b00-4660-a778-d06835d77f2c/8IN1eskTjD.json"
lottie_Gallery = load_lottieurl(Galley_Url)
#st_lottie(lottie_Gallery,speed=2, reverse=False, loop=True, quality="medium", height=150, width=150,
#key=None )
Check_Url = "https://lottie.host/4cdd2732-6ed4-497d-9a95-8c311dae98f2/iVzSMcOcCx.json"
lottie_Check = load_lottieurl(Check_Url)
col1, col2, col3 = st.columns(3)

with col1:
    st_lottie(lottie_Gallery,speed=2, reverse=False, loop=True, quality="medium", height=150, width=150,
    key=None )
with col2:
    st_lottie(Check_Url,speed=2, reverse=False, loop=True, quality="medium", height=150, width=150,
    key=None )
with col3:
    st_lottie(lottie_Gallery,speed=2, reverse=False, loop=True, quality="medium", height=150, width=150,
    key=None )

st.title("TGYYMP Performance Overview") 
st.subheader("Programme logbook")
st.info("SMART GOALS")
#Removal of logo
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#Gallery code
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button
    
#st.button('Click to view schedule', on_click=click_button)
Gallery_code = st.button('*Click to view schedule*', on_click=click_button)
if st.session_state.button:
    weekly_p = st.slider('Weekly Plan', 0, 25, 52)
    # The message and nested widget will remain on the page. Including Gallery
    st.write(weekly_p, 'Weeks')
    GYYM_c = st.text_input("Enter GYYM of choice: ")
    TGYYMP_date = st.date_input("Today's Date ", datetime.date(2023, 11, 29))
    txt = st.text_area("SHORT TERM",
"Specific ... Measurable ... Attainable ... Realistic ... Time-Bound ...",
)
    txt_2 = st.text_area("MEDIUM TERM","Specific ... Measurable ... Attainable ... Realistic ... Time-Bound ...",
)
    txt_3 = st.text_area("LONG TERM",
"Specific ... Measurable ... Attainable ... Realistic ... Time-Bound ...",
)
    Personal_Trainer = st.checkbox('Personal Trainer')
    if Personal_Trainer:
        st.checkbox("Male") 
        st.checkbox("Female")
        st.text_input("Personal Trainer Name:")

    Overview_1 = st.expander("Overview")
    with st.expander("Overview"):
        st.write(weekly_p, 'Weeks')
        GYYM_c
        TGYYMP_date
        "|Short term|" 
        txt 
        "|MEDIUM TERM|"
        txt_2
        "|LONG TERM|"
        txt_3 
        text_contents = f" Weeks..<...>.,{GYYM_c}..<...>, ,{TGYYMP_date}...<....>,  |(Short term)|, <{txt}>, |(Medium term)|,<{txt_2}>, |(long term)|, <{txt_3}>"

        st.download_button('File', text_contents)
#Login
