import pandas as pd
import streamlit as st

df = pd.read_excel("https://1drv.ms/x/c/84b14527e3f20dbd/EbsQ-kL-xUhLhDzsnTcE8DQBl16BrzKij7Oq1_wzdoey8Q?e=yxwwjz", sheet_name="Alusvia")

st.write("Welcome to Shopping List!")

st.dataframe(df)