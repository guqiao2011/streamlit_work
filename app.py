import streamlit as st 

import requests

url = "http://www.baidu.com"
resp = requests.get(url)
resp.encoding = 'utf8'
st.write(resp.text)

st.write("""
# Sales model
Below are our sales predictions
""")
