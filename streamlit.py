import time
import streamlit as st
import numpy as np

from PIL import Image
import urllib.request
from utils import *

<<<<<<< HEAD
=======
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

>>>>>>> 0d9d9e3a81191569db926c0958467dd4ca0718d2
labels = gen_labels()




st.title('Garbage Classification')

with st.expander("About us:"):
    st.write(
        "Hello, we are Jan, Narin and Siyu. We are student of business informatics and are happy to attend the course ML4B and learn more about the world of machine learning.")

with st.expander("Our Goal:"):
    st.write(
        "Our project is to train a model to classify images of garbage correctly and compare different approaches on different dataset sizes.")

<<<<<<< HEAD
html_temp = '''
    <div style =  padding-bottom: 20px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
    <center><h1>Garbage Segregation</h1></center>

    </div>
    '''

st.markdown(html_temp, unsafe_allow_html=True)
=======


>>>>>>> 0d9d9e3a81191569db926c0958467dd4ca0718d2
html_temp = '''
    <div>
    <h2></h2>
    <center><h3>Please upload Waste Image to find its Category</h3></center>
    </div>
    '''
st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown(html_temp, unsafe_allow_html=True)
opt = st.selectbox("How do you want to upload the image for classification?\n",
                   ('Please Select', 'Upload image via link', 'Upload image from device'))
if opt == 'Upload image from device':
    file = st.file_uploader('Select', type=['jpg', 'png', 'jpeg'])
    st.set_option('deprecation.showfileUploaderEncoding', False)
    if file is not None:
        image = Image.open(file)

elif opt == 'Upload image via link':

    try:
        img = st.text_input('Enter the Image Address')
        image = Image.open(urllib.request.urlopen(img))

    except:
        if st.button('Submit'):
            show = st.error("Please Enter a valid Image Address!")
            time.sleep(4)
            show.empty()

try:
    if image is not None:
        st.image(image, width=300, caption='Uploaded Image')
        if st.button('Predict'):
            img = preprocess(image)

            model = model_arc()
<<<<<<< HEAD
            model.load_weights("../weights/model.h5")
=======
            model.load_weights("./weights/model.h5")
>>>>>>> 0d9d9e3a81191569db926c0958467dd4ca0718d2

            prediction = model.predict(img[np.newaxis, ...])
            st.info('Hey! The uploaded image has been classified as " {} waste " '.format(
                labels[np.argmax(prediction[0], axis=-1)]))
except:
    pass

