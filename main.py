"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Mental-Ailment Detection Degree',
    page_icon = 'img_bg\Mental_bg.jpg',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

# Import pages
from Tabs import home, data, predict



# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    
    #"About me": about
}
with open('wave.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# Create a sidebar
# Add title to sidear
#st.sidebar.title("AAP Navigation")

# Create radio option to select the page
page = st.radio("*Welcome to Health Assistance System!!*", list(Tabs.keys()))



# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
