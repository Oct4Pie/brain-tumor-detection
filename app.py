import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'model')))
import streamlit as st
import streamlit.components.v1 as html_components
from pages import home
from pages import about
from pages import github
from pages import components
from pages import try_it



routes = {
    "Home": home.main,
    "Try it out": try_it.main,
    "About": about.main,
    "GitHub": github.main,
}

pages = list(routes.items())
# current_page = pages[0]
def format_func(page):
#     print(page)
#     current_page = pages[list(routes.keys()).index(page[0])]
#     return current_page[0]
    return page[0]

page = st.sidebar.selectbox(
            'Menu',
            pages,
            index=0,
            format_func=format_func,
            # on_change=current_page[1]
            
        )

page[1]()