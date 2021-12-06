import streamlit as st
from .components import title
import streamlit.components.v1 as html_components

def main():
    html_components.html(title())
    st.title("GitHub")