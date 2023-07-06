import streamlit as st
import pandas as pd
import snowflake.connector

con1 = snowflake.connector.connect(**st.secrets["snowflake"])
cur1 = con1.cursor()
cur1.execute("select top 100 state, county from COVID19_EPIDEMIOLOGICAL_DATA.PUBLIC.DEMOGRAPHICS")

st.title('View Raw Data')
