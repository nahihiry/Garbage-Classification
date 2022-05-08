import streamlit as st
import pandas as pd
import numpy as np


st.title('Garbage Classification')

st.markdown('Hello, we are Jan, Narin and Siyu. Our project is to train a model to classify images of garbage correctly '
          'and compare different approaches on different dataset sizes.', True)

# Example cardboard garbage image
from PIL import Image
image = Image.open('cardboard1.jpg')

st.image(image, caption='Example cardboard garbage image')

uploaded_file = st.file_uploader("Choose an image...")
