import streamlit as st
import pandas as pd

st.set_page_config(page_title="Health Coach", page_icon=":heart:", layout="wide" )

with st.container():
    st.title ("HealaaathCoach :heart: :running:")
    st.subheader("hey")

st.sidebar.success("select a page above")

import urllib.request, json

resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
st.print(price)
