import streamlit as st

def set_css(css_path):
    """
    Set the CSS file to use.
    """
    css_file = open(css_path, "r").read()
    st.markdown('<style>{}</style'.format(css_file), unsafe_allow_html=True)
