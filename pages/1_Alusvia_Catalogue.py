import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide",
                    page_title="Alusvia Catalogue")
                    
df = pd.read_excel("Wilder at Catalogue.xlsx", sheet_name="Alusvia", header = 1, usecols="B:J")
#conn = st.connection("gsheets", type=GSheetsConnection)
st.title("Alusvia Catalogue") 
#df = conn.read(worksheet = "Alusvia",usecols=[1, 9],nrows=3,)    
st.write("Welcome to the Shopping List!")
st.link_button("Source", "https://1drv.ms/x/c/84b14527e3f20dbd/IQC7EPpC_sVIS4Q87J03BPA0AZdega8yoo-zqtf8M3aHsvE?e=g2qENB")

cart = st.dataframe(df, 
            row_height=120, 
            hide_index=True,
            key="Items",
            selection_mode="multi-row",
            on_select="rerun"
            )

selections = cart.selection["rows"]
#st.write(selections)