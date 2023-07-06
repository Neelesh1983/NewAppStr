import streamlit as st
import pandas as pd

st.title('View Raw Data')

import snowflake.connector
from snowflake.connector import ProgrammingError

con = snowflake.connector.connect(**st.secrets["snowflake"])
