import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "model")))
import streamlit as st
from pages import home
from pages import about
from pages import github
from pages import try_it


routes = {
    "Home": home.main,
    "Try it out": try_it.main,
    "About": about.main,
    "GitHub": github.main,
}

# st.markdown(
#     "<head> <meta http-equiv=\"Content-Security-Policy\" \"> </head>",
#     unsafe_allow_html=True,
# )


st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/Oct4Pie/brain-tumor-detection",
        "Report a bug": "https://github.com/Oct4Pie/brain-tumor-detection/issues",
        "About": "Detecting brain tumors using *deep Convolutional Neural Networks*. Written by Mehdi Hajmollaahmad Naraghi",
    },
)
st.markdown(
    """
<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.min.js" />
<script src="https://raw.githubusercontent.com/darcyclarke/Repo.js/master/repo.min.js" />""",
    unsafe_allow_html=True,
)


pages = list(routes.items())
# current_page = pages[0]
def format_func(page):
    #     print(page)
    #     current_page = pages[list(routes.keys()).index(page[0])]
    #     return current_page[0]
    return page[0]


page = st.sidebar.selectbox(
    "Menu",
    pages,
    index=0,
    format_func=format_func,
    # on_change=current_page[1]
)

page[1]()
