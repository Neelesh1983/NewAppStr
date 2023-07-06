import streamlit as st
import pandas as pd
import snowflake.connector as sncon

con1 = sncon.connect(**st.secrets["snowflake"])
cur1 = con1.cursor()
cur1.execute("select top 100 state, county from DEMOGRAPHICS")

st.title('View Raw Data')
