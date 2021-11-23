import streamlit as st
import requests
import pandas as pd
import numpy as np

'''
# YBABBABYYBABBABYYBABBABYYBABBABY
'''
st.markdown("""#  -- - BABY - --
## Welcome to BABY!
##
""")

art_type = st.radio('Today BABY will write you...',
                    ('a poem', 'a haiku', 'a rapsong', 'nothing'))

topic = st.text_input('I want to talk about...', 'influence')

url = 'https://taxifare.lewagon.ai/predict'
X = dict(param1=art_type, param2=topic)

# 3. Let's call our API using the `requests` package...
response = requests.get(url, params=X)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
response.json()

## Finally, we can display the prediction to the user
st.markdown("""
## Here is you poem:
""")
#st.text(round(response.json()['prediction'], 2))
st.text("Nononono, Nononono")
