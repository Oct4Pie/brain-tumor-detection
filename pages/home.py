import streamlit as st
import os
import numpy as np
import cv2
from PIL import Image
import streamlit.components.v1 as html_components
from .utils import set_css
from .components import title
from predictor import get_model
from mask import crop_img

# @st.cache
def load_model():
    model, acc, loss = get_model(6)
    return model, acc, loss


def main():
    set_css("pages/css/streamlit.css")
    html_components.html(title())
    st.write("These are pre-cropped MRI scan samples. They were used to valdiate the model.\n")
    samples = os.listdir("pages/samples")
    option = st.selectbox("Select an image for analysis", (range(1, len(samples) + 1)))
    collection = []
    for i in range(0, len(samples), 3):
        collection.append(st.columns(3))

    if i < len(samples) - 3:
        collection.append(st.columns(len(samples) - i))

    index = 0
    for column_list in collection:
        for i in range(len(column_list)):
            column_list[i].image(Image.open(f"pages/samples/{samples[index]}"))
            column_list[i].subheader(index + 1)
            index += 1

    if st.button("Analyze"):
        with st.spinner(text="Analyzing..."):
            model, acc, loss = load_model()
            image = cv2.imread(f"pages/samples/{samples[option-1]}")
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[-1]
            img = np.array([cv2.resize(image, (32, 32))])
            prediction = model.predict(img)

            st.write(
                """
                #### Mask Threshold
                """
            )

            st.image(thresh, caption=option)

            st.write(
                """
                        #### Prediction
                        """
            )
            st.image(image, caption=option)
            if prediction[0][0] == 1:
                st.write(f"Sample {option} has a tumor")

            if prediction[0][0] == 0:
                st.write(f"Sample {option} has no tumor")
            st.write(f"Accuracy: {acc*100:.2f}%")
