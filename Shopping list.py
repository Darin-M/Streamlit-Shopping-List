import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

@st.cache_data
def main():
    st.set_page_config(layout="wide",
    page_title="Home")
    st.title("Wilder Companion") 
    st.write("Welcome to the Wilder Companion app! Here you wll be able to find a range of handy tools for your d&d game to help make things a little bit easier!")

    st.sidebar.success("Select a page above.")

if __name__ == "__main__":
    main()