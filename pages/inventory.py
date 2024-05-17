import streamlit as st
from navigation import SideBar
class streamlit_page_config:
    st.set_page_config(
        page_title="INVENTORY",
        layout= "wide",
        initial_sidebar_state='auto',

    )

    st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

    hide_footer_style = '''<style>.reportview-container .main footer {visibility: hidden;} </style>'''
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    hide_menu_style = '''<style> #MainMenu {visibility: hidden;} </style>'''
    st.markdown(hide_menu_style, unsafe_allow_html=True)

streamlit_page_config()
side_bar = SideBar()
side_bar.authenticated_menu()