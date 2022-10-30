import requests
import streamlit as st

url= 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

name= data['Meta Data']['2. Symbol']
open = data['Time Series (Daily)']['2022-10-28']['1. open']
st.write(name)
st.write(open)


st.write("simple stock price")