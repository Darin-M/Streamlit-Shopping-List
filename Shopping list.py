import pandas as pd
import streamlit as st

df = pd.read_excel("Wilder at Catalogue.xlsx", sheet_name="Alusvia")

st.write("Welcome to Shopping List!")


st.dataframe(df)
