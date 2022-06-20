import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

dir = './Dataset/'
labels = os.listdir(dir + '/Garbage classification/Garbage classification/')

st.title('Garbage Classification')


with st.expander("About us:"):
    st.write(
        "Hello, we are Jan, Narin and Siyu. We are student of business informatics and are happy to attend the course ML4B and learn more about the world of machine learning.")

with st.expander("Our Goal:"):
    st.write(
        "Our project is to train a model to classify images of garbage correctly and compare different approaches on different dataset sizes.")



option = st.selectbox('Choose an image', ('cardboard', 'glass', 'metal', 'paper', 'plastic'))


type_path = os.path.join(dir + 'Garbage classification/Garbage classification/', option)
list_of_images = os.listdir(type_path)
image_box = st.selectbox("Sample", list_of_images)
sample_path = os.path.join(type_path, image_box)
image = Image.open(sample_path)
st.image(image, caption=image_box)