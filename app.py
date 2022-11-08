import streamlit as st 
import streamlit.components.v1 as components
import requests


url = "http://www.baidu.com"
resp = requests.get(url)
resp.encoding = 'utf8'
#st.write(resp.text)

components.html(
  resp.text,
  height=600)



#st.write("hello world")
