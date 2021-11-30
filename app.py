import streamlit as st
import requests
import pandas as pd
import numpy as np

CSS = """
h1 {
    color: #B8860B;
}
h3 {
    color: #2F4F4F;
}

.stApp {
    background-size: cover;
    background-color: #F0F8FF;

}
"""

#old     background-image: url(https://cdn.mos.cms.futurecdn.net/ZsQmSHKYueHSDgJ4r3KHhk-970-80.gif);
#old2    background-image: url(https://upload.wikimedia.org/wikipedia/en/c/ce/DancingBaby.jpg);

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'''
# YBABBABYYBABBABYYBABBABYYBAB
'''
st.markdown("""#  -- - BABY - --
## Welcome to BABY!
##
""")

model_type = st.radio(
    'Which model do you want to try?',
    ('ada', 'curie', 'babbage', 'davinci',
     'curie:ft-user-6qfzuqjhvk29sbtb6ezmcw63-2021-11-27-16-36-49'))

# hatespeech = st.radio('Activate Hate Speech Detecor', (True, False))

# temperature = st.slider('Select a temperature', 1, 10, 1)

n = st.slider('Select number of generations', 1, 3, 1)

# max_tokens = st.slider('Select max tokens', 25, 75, 1)

secrets = st.text_input('Password', '')

'''
### BABY, please write me a beautiful piece of art about... (Separate topics by a comma (3 topics max))
'''
prompt = st.text_input('', 'flowers, philosophy')

col1, col2 = st.columns(2)

with col1:
    st.subheader("...in the lyrical form of a...")
    answer_type = st.radio('',
                       ('haiku',
                        'rap song',
                        'classical poem',
                        'bob dylan song'))

with col2:
    st.subheader("...written by...")
    personality_type = st.radio('', (
        'greta thunberg',
        'elon musk',
        'michelle obama',
        'justin bieber',
        'an artificial intelligence'
    ))

url = 'https://morning-citadel-09821.herokuapp.com/predict'

X = dict(model=model_type,
         prompt=prompt,
         personality_type=personality_type,
         secret=secrets,
         _type=answer_type)

# 3. Let's call our API using the `requests` package...
#response = requests.get(url, params=X)
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
#response.json()

def call_api():
    response = requests.get(url, params=X)
    return response.json()["response"]


if st.button('Feed BABY.'):
    poem = call_api()
    # for poem in poems:
    # poem = poem.replace("\n===", "")
    st.markdown(f'## This is a {answer_type}, written by the fake personality of {personality_type} about {prompt}:')
    st.markdown(f'## {poem}')

'''### ____BABY____ is:

Users’ generative AI poetry InterFace
/ a computational system, where mathematics meets language and logic meets power
/ by Rhea Dally, Guilliaume De Sa, Marco Zausch, Tim Seifert
'''
