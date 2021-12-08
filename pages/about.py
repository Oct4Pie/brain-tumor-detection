import streamlit as st
from .components import title
from .utils import set_css
import streamlit.components.v1 as html_components

def main():
    html_components.html(title())
    set_css("pages/css/streamlit.css")
    st.markdown("<h4 style='text-align: center'>About</h4>", unsafe_allow_html=True)
    about_text = """
    This app is written in Python 3 using the Tenserflow library 
    and uses Keras to build a neural network to classify images.
    Keras is a high-level API for TensorFlow. In this case,
    a Convolutional Neural Network was created using multiple layers
    of convolutional and pooling layers. Then, the network was trained
    using datasets found in Kaggle. Importantly, the traning data was
    cleaned using the [mask.py](https://github.com/Oct4Pie/brain-tumor-detection/blob/main/model/mask.py)
    script and cropped to unnecessary backgrounds. After the training,
    the model and its weights were saved to a file. The model can be
    loaded using the [get_model(num)](https://github.com/Oct4Pie/brain-tumor-detection/blob/f13044f11e797a90ed73b2bbe94ab7a7502f02f5/model/predictor.py#L24)
    where num is the number of the model to be loaded. This interface is
    built using Streamlit and uses this mechanism to allow for a fast and
    intuitive analysis of given data.
    """
    st.write(about_text)
    st.markdown("<a href='https://github.com/Oct4Pie/' target='_blank'><h6 style='text-align: center'>by Mehdi Hajmollaahmad Naraghi</h6></a>", unsafe_allow_html=True)