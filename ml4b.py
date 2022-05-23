import streamlit as st
import pandas as pd
import numpy as np
import opendatasets as od


st.title('Garbage Classification')

dataset = "https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification?resource=download"
od.download(dataset)

st.markdown('Hello, we are Jan, Narin and Siyu', True)

with st.expander ("The problem:")
st.write("Many people dont know how to seperate their waste correctly. Most of the countries dont have a law that requires their inhabitants to seperate their trash, which is why lots of people dont even know how recycling works. Recycling, however, is an important point in order to protect the environment.") 

with st.expander ("Our Goal:")
st. write ("Our project is to train a model to classify images of garbage correctly and compare different approaches on different dataset sizes. The purpose of our app is to to separate waste properly. Our dataset is divided into six categories: cardboard, glass, metal, paper, plastic and a test dataset. We  

# Example cardboard garbage image
from PIL import Image
image = Image.open('cardboard1.jpg')

st.image(image, caption='Example cardboard garbage image')

uploaded_file = st.file_uploader("Choose an image...")
