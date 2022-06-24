import streamlit as st
import os


def app():
    st.title("Project Garbage Classification")

    st.subheader("Objective: ")
    st.markdown(
        "The main Objective of this project is to use `Machine Learning` to categorize the garbage image into different classes correctly. ",
        True)

    st.subheader("About us: ")
    st.markdown(
        "Hello, we are Jan, Narin and Siyu. We are student of business informatics and are happy to attend the course ML4B and learn more about the world of machine learning. ",
        True)


    st.markdown("<hr/>", True)

    # st.subheader("Description:")
    # st.markdown("This Project uses `Fine Tuned InceptionV3 Model` which is a Pre-Trained CNN Model from Keras.", True)
    # st.markdown("It Gave the `Highest Accuracy of 96%` while classifying image from test set.", True)
    #
    # st.markdown("<hr/>", True)
