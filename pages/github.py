import streamlit as st
from .utils import set_css, set_js
from .components import title, github_iframe, github_card
import streamlit.components.v1 as html_components

 
def main():

    # script = """
    # $(function() {
    #     $('#github-widget').repo({
    #         user: 'oct4pie',
    #         name: 'brain-tumor-detection'
    #     })
    # });
    # """
    # set_js(script, "github-widget")
    set_css("pages/css/streamlit.css")
    html_components.html(title())
    html_components.html(github_card(), height=300)

    col1 = st.columns(1)
    with col1[0]:
        html_components.html(github_iframe(), height=500, scrolling=True)
