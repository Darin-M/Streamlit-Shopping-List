import pandas as pd
import streamlit as st

df = pd.read_excel("Wilder at Catalogue.xlsx", sheet_name="Alusvia", header = 2, usecols="B:I")

st.write("Welcome to Shopping List!")


st.dataframe(df)
