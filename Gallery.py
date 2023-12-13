import streamlit as st
import datetime
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
Gallery_code = st.button('Click to view schedule', on_click=click_button)
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

    st.write(f'You wrote {len(txt)} characters.')

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

        st.download_button('Edit', text_contents)
#Login
