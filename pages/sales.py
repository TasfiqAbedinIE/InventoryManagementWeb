import streamlit as st
from navigation import SideBar
from datetime import datetime
class streamlit_page_config:
    st.set_page_config(
        page_title="SALES",
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

@st.experimental_fragment(run_every="60s")
def intro_section():
    date = datetime.today()
    st.html(f"""
        <div class="container">
            <div class="component">USER ID: {st.session_state.get("id")}</div>
            <div class="component">{date.strftime("%d-%B-%Y, %H:%M %p")}</div>
        </div> 
    """)

intro_section()