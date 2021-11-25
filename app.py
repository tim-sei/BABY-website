from SimpleTaxiFare.trainer import MODEL_NAME
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

temperature = st.slider('Select a temperature', 1, 10, 1)

prompt = st.text_input('I want to know: Can beta.BABY give the right answer to my joke...', 'Type in my joke...')

secrets = st.text_input('Password', 'write password here')

url = 'https://morning-citadel-09821.herokuapp.com/predict'
X = dict(model=model_type, prompt=prompt, secret=secrets, temperature=temperature/10)

# 3. Let's call our API using the `requests` package...
#response = requests.get(url, params=X)
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
#response.json()

def call_api():
    response = requests.get(url, params=X)
    return response.json()["response"].replace("\n===", "")


if st.button('Answer my joke'):
    st.markdown(f'## {call_api()}')

## Finally, we can display the prediction to the user
#st.text(response.json())
#st.text("Nononono, Nononono")
