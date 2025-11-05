import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

@st.cache_data
def main():
    st.set_page_config(layout="wide",
                       page_title="Alusvia Catalogue")
                       
    df = pd.read_excel("Wilder at Catalogue.xlsx", sheet_name="Alusvia", header = 1, usecols="B:J")
    #conn = st.connection("gsheets", type=GSheetsConnection)
    st.title("Alusvia Catalogue") 
    #df = conn.read(worksheet = "Alusvia",usecols=[1, 9],nrows=3,)    
    st.write("Welcome to the Shopping List!")

    st.dataframe(df, 
                 row_height=80, 
                 hide_index=True,
                 key="Items",
                 selection_mode="single-row",
                 on_select="rerun"
                 )

if __name__ == "__main__":
    main()