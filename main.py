import streamlit as st
from sign_inup_screen import SignInUp

class Page_config:
    def __init__(self):
        super().__init__()
        st.set_page_config(
            page_title="STORMY",
            initial_sidebar_state="collapsed"
        )
        st.markdown(
            """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
        </style>
        """,
            unsafe_allow_html=True,
        )

Page_config()
SignInUp()

