import os


import streamlit as st
import plotly.express as px
import predictor


def app():
    st.write("# Project Garbage Classification")

    st.write("## Upload Image in .jpg format")
    uploaded_image = st.file_uploader("", type=["jpg"])

    st.write("## Uploaded Image")

    if uploaded_image:
        st.image(uploaded_image)

        button = st.button("Classify", key=None)

        if button:
            prediction, predicted_class = predictor.predict(uploaded_image)

            labels = {0: 'glass', 1: 'metal', 2: 'paper', 3: 'plastic', 4: 'trash'}

            classes = []
            prob = []
            for i, j in enumerate(prediction[0], 0):
                classes.append(labels[i].capitalize())
                prob.append(round(j * 100, 2))

            fig = px.bar(x=classes, y=prob,
                         text=prob, color=classes,
                         labels={"x": "Material", "y": "Probability(%)"})

            st.markdown("#### Probability Distribution Bar Chart", True)
            st.plotly_chart(fig)

            st.markdown(
                f"#### The Image Is Classified As`{predicted_class.capitalize()}` With A Probability Of `{max(prob)}%`",
                True)

    else:
        st.write("#### No Image Was Found, Please Retry!!!")