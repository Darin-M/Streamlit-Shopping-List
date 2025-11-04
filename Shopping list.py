import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

@st.cache_data
def main():
    st.set_page_config(layout="wide",
                       menu_items={"Excel Sheet": "https://1drv.ms/x/c/84b14527e3f20dbd/EbsQ-kL-xUhLhDzsnTcE8DQBl16BrzKij7Oq1_wzdoey8Q?e=emMLTV"})
    df = pd.read_excel("Wilder at Catalogue.xlsx", sheet_name="Alusvia", header = 1, usecols="B:J")
    #conn = st.connection("gsheets", type=GSheetsConnection)

    #df = conn.read(worksheet = "Alusvia",usecols=[1, 9],nrows=3,)    
    st.write("Welcome to Shopping List!")

    st.dataframe(df, row_height=80)

if __name__ == "__main__":
    main()