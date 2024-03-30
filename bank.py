         
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Streamlit page setup
st.set_page_config(page_title='bankserver',
                   page_icon=":bank")

# Initialization of session state
if 'authority' not in st.session_state:
    st.session_state['authority'] = False

# Function to display login page
def display_login():
    st.title(":blue[Banking Application]")
    username = st.text_input("Username", placeholder="Enter Your username")
    passkey = st.text_input("Password", type="password", placeholder="Enter your password")
    submit_button = st.button("Login")

    if username == "admin" and passkey == "Meena" :
        st.session_state["authority"] = True
    if submit_button:
        if  st.session_state["authority"] == True:
          st.success("logged in successfully")
          st.experimental_rerun()
        else:
            st.error("invalid username or password",icon="🚨")
            
       
# Function to display session page
def display_session():
    with st.sidebar:
        st.header(":key: Navigation")
        selected_page = option_menu("Choose Session",["Session 1", "Session 2"],
                                    icons=["bar_chart_line","bust_in_silhouette"])

    if selected_page ==  'Session 1':
        st.header(":clipboard: Bank users and their details")
        df = pd.read_csv("bankinfo.csv")
        st.dataframe(df)

    elif selected_page == 'Session 2':
        st.header(":bust_in_silhouette: User Details")
        username = st.text_input("Enter your name",placeholder="Enter Your username")

        if st.button("Fetch Details"):
            df = pd.read_csv("bankinfo.csv")
            user_details = df[df['Name'] == username]

            if len(user_details) == 0:
                st.error("User not found")
            else:
                st.success("User found")
                row = user_details.iloc[0]  # Select only the first matching user
                with st.expander(" :blue[User Status] "):
                    st.write("👤 :blue[**Name:**] ", row['Name'])
                    st.write("📅 :blue[**Date Joined:**] ", row['Date Joined'])
                    st.write("💰 :blue[**Balance:**] ", row['Balance'])
                    st.write("👔 :blue[**Job Classification:**] ", row['Job Classification'])
                    st.write("🌍 :blue[**Region:**] ", row['Region'])
                    st.write("⚖️ :blue[**Gender:** ]", row['Gender'])
                    st.write("🎂 :blue[**Age:**] ", row['Age'])
                    
    col1,col2,col3=st.columns(3)
    with col2:
        if st.button("Logout"):
            st.session_state['authority'] = False
            st.experimental_rerun()

# Check if user is logged in
if not st.session_state['authority']:
    display_login()
else:
    display_session()

