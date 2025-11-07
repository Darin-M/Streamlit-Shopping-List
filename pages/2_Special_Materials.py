import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

@st.cache_data
def main():
    st.set_page_config(layout="wide",
                       page_title="Special Materials")
                       
    df = pd.read_excel("Wilder at Catalogue.xlsx", sheet_name="Special Materials", header = 2, usecols="B:K")
    #conn = st.connection("gsheets", type=GSheetsConnection)
    st.title("Materials Index") 
    #df = conn.read(worksheet = "Alusvia",usecols=[1, 9],nrows=3,)    
    st.write("Explore the strange and wonderful materials of the world!")

    st.dataframe(df, row_height=80, hide_index=True)

if __name__ == "__main__":
    main()
