import streamlit as st
import pandas as pd
import snowflake.connector as sncon

con1 = sncon.connect(
  user = 'Neelesh2023',
  password = 'Neelesh@2023',
  account = 'vi98550.ap-southeast-1.aws',
  warehouse = 'COMPUTE_WH',
  database = 'COVID19_EPIDEMIOLOGICAL_DATA',
  schema = 'Public')
cur1 = con1.cursor()
cur1.execute("select top 100 state, county from DEMOGRAPHICS")

st.title('View Raw Data')
