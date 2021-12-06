import streamlit as st
import os
import numpy as np
import cv2
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
    set_css('pages/css/streamlit.css')
    html_components.html(title())
    image_bytes = st.file_uploader("Upload a brain MRI scan image", type = ['png', 'jpeg', 'jpg'])
    def format_func(item):
        return item
        

    if image_bytes:
        array = np.fromstring(image_bytes.read(), np.uint8)
        image = cv2.imdecode(array, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (128, 128))
        st.write("""
                #### Brain MRI scan image
                """)
        st.image(image)
    
    if st.button("Analyze"):
            with st.spinner(text='Analyzing...'):
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                img = crop_img(gray, image, None)
                cv2.imwrite('temp.png', img)
                model, acc, loss = load_model()
                img_mask = crop_img(gray, image, None)
                gray_mask = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
                thresh = cv2.threshold(gray_mask, 0, 255, cv2.THRESH_OTSU)[-1]
                img = cv2.resize(img, (32, 32))
                img = np.array([img])
                prediction = model.predict(img)

                st.write("""
                #### Mask Threshold
                """)

                st.image(cv2.resize(thresh, (128, 128)))

                st.write("""
                            #### Prediction
                            """)
                st.image(cv2.resize(img_mask, (128, 128)))
                if prediction[0][0] == 1:
                    st.write(
                        f"The sample has a tumor"
                    )

                if prediction[0][0] == 0:
                    st.write(
                        f"The sample has no tumor"
                    )
                st.write(f"Accuracy: {acc*100:.2f}%")
