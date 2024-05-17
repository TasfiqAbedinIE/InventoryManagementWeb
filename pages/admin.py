import streamlit as st
from navigation import SideBar

class streamlit_page_config:
    st.set_page_config(
        page_title="ADMIN",
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

from serverManagement import get_company_name
company_name = get_company_name()
print(company_name)

r1 = st.container()
with r1:
    st.markdown('<p class="main_title">ADMIN PANEL</p>', unsafe_allow_html=True)
    st.markdown("")

r2 = st.container()
@st.experimental_dialog("ADD ITEM")
def add_item_modal():
    add_item = st.selectbox("Select Option", ["Brand Name", "Medicine Type"], key="add_item_selectbox")
    new_name = st.text_input(f"{'New Brand Name' if add_item=='Brand Name' else 'New Med Type'}", key="new_name")

with r2:
    st.button("ADD ELEMENTS", on_click=add_item_modal)
    r2c1, r2c2, r2c3 = st.columns(3)
    with r2c1:
        with st.container(border=False, height=300):
            st.markdown('<p class="sub_title">BRANDS</p>', unsafe_allow_html=True)
            column_config = {
                "Cname": "BRAND",
                "Cid": "ID"
            }
            company_list = st.dataframe(company_name, column_config=column_config, use_container_width=True)

    with r2c2:
        with st.container(border=False, height=300):
            st.markdown('<p class="sub_title">MEDICINE TYPE</p>', unsafe_allow_html=True)
            column_config = {
                "Mtype": "MED TYPE",
                "Mid": "ID"
            }
            med_type_list = st.dataframe(company_name, column_config=column_config, use_container_width=True)

r3 = st.container()
with r3:
    st.markdown('<p class="sub_title">USER DETAILS</p>', unsafe_allow_html=True)
