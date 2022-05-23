import streamlit as st
import pandas as pd
import numpy as np
import os

dir = './Dataset/'
labels = os.listdir(dir + '/Garbage classification/Garbage classification/')

st.title('Garbage Classification')


with st.expander("About us:"):
    st.write(
        "Hello, we are Jan, Narin and Siyu. We are student of business informatics and are happy to attend the course ML4B and learn more about the world of machine learning.")

with st.expander("Our Goal:"):
    st.write(
        "Our project is to train a model to classify images of garbage correctly and compare different approaches on different dataset sizes.")

# Example cardboard garbage image
from PIL import Image

image = Image.open('cardboard1.jpg')

st.image(image, caption='Example cardboard garbage image')

option = st.selectbox('Choose an image', ('cardboard', 'glass', 'metal', 'paper', 'plastic'))
st.write('You selected:', option)
