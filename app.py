import streamlit as st
import requests
import pandas as pd
import numpy as np

CSS = """
h1 {
    color: red;
}
h2 {
    color: green;
}

.stApp {
    background-image: url(https://cdn.mos.cms.futurecdn.net/ZsQmSHKYueHSDgJ4r3KHhk-970-80.gif);
    background-size: cover;
    background-color: black;

}
"""
if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'''
# YBABBABYYBABBABYYBABBABYYBAB
'''
st.markdown("""#  -- - BABY - --
## Welcome to BABY!
##
""")

model_type = st.radio('Which model do you want to try?',
                    ('ada', 'curie', 'babbage', 'davinci'))

hatespeech = st.radio('Activate Hate Speech Detecor', (True, False))

temperature = st.slider('Select a temperature', 1, 10, 1)

n = st.slider('Select number of generations', 1, 3, 1)

prompt = st.text_input('Write a poem about...', '')

secrets = st.text_input('Password', '')

url = 'https://morning-citadel-09821.herokuapp.com/predict'

X = dict(model=model_type, prompt=prompt, secret=secrets, temperature=temperature/10, n=n, HateSpeechDetector=hatespeech)

# 3. Let's call our API using the `requests` package...
#response = requests.get(url, params=X)
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
#response.json()

def call_api():
    response = requests.get(url, params=X)
    return response.json()["response"]


if st.button('Write me AI poesy.'):
    poems = call_api()
    for poem in poems:
        st.markdown(f'## {poem.replace("\n===", "")}')

## Finally, we can display the prediction to the user
#st.text(response.json())
#st.text("Nononono, Nononono")
