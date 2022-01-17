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
    st.markdown("<h4 style='text-align: center'>Abstract</h4>", unsafe_allow_html=True)
    abstract_text = """
    Brain cancers (e.g. glioblastomas) are some of the deadliest types of 
    cancers and are some of the most difficult to treat due to their anatomical 
    location. Early tumor detection is crucial for a good prognosis but oftentimes 
    the diagnosis is difficult because the tumor is too small and not easily 
    detectable. Traditional diagnosis techniques include a brain scan (i.e. MRI), 
    which can be time-consuming for doctors to analyze. An alternative, efficient 
    technique for diagnosis (analysis of the MRI) is the use of machine learning, 
    which can be used with an image classifier for fast and accurate detection. 
    Here, we used open-source MRI datasets that are trimmed and resized for accurate
    results. We implement TensorFlow's Convolutional Neural Networks (CNN) as the 
    architecture for our model. The images that we used in our algorithm were made 
    up of 46% that had tumors and 54% that were not cancerous. The program takes 
    about 3.47 seconds to load the model and produce predictions. Our model has a 
    validation loss of 0.122 and a 99.50% max validation accuracy. Although our 
    model focuses on brain tumors, its use can be extended to other types of 
    cancers that are diagnosed with similar methods (e.g MRI). The program has 
    a graphic interface built using Streamlit and is hosted at 
    https://share.streamlit.io/oct4pie/brain-tumor-detection/main/app.py. 
    Also, the source code is located at https://github.com/oct4pie/brain-tumor-detection. """
    st.write(abstract_text)
    st.markdown("<p class='git_link'> <a href='https://github.com/Oct4Pie/' target='_blank'><h6 style='text-align: center'>by Mehdi Hajmollaahmad Naraghi</h6></a> </p>", unsafe_allow_html=True)