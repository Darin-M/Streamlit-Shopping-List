import pandas as pd
import streamlit as st

@st.cache_data
def main():
    df = pd.read_excel("Wilder at Catalogue.xlsx", sheet_name="Alusvia", header = 1, usecols="B:J")

    st.write("Welcome to Shopping List!")

    st.table(df)

if __name__ == "__main__":
    main()