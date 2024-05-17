import streamlit as st
from time import sleep


class SideBar:
    def __init__(self):
        super().__init__()

    def logout(self):
        # st.session_state.logged_in = False
        st.info("Logged out successfully!")
        sleep(0.5)
        st.switch_page("main.py")

    def authenticated_menu(self):
        user_name = st.session_state.get("username")
        st.sidebar.markdown(f"Welcome, <b>{user_name.capitalize()}</b>", unsafe_allow_html=True)
        st.sidebar.markdown("")
        st.sidebar.page_link("pages/sales.py", label="SALES", icon="🏡")
        st.sidebar.page_link("pages/inventory.py", label="INVENTORY", icon="📋")
        if st.session_state.get("admin") == True:
            st.sidebar.page_link("pages/admin.py", label="ADMIN", icon="🛠️")

        st.markdown("")
        st.markdown("")
        st.markdown("")
        if st.sidebar.button("Log out"):
            self.logout()
            st.markdown("""
                                        <style>
                                        div.stButton > button:first-child {
                                            background-color: #d90429;
                                            color: #ffffff;
                                            border-color: #d90429;
                                            width: 7em;
                                            margin-left: 0.5em;
                                        }
                                        div.stButton > button:first-child:hover {
                                            background-color: #ef233c;
                                        }
                                        </style>""", unsafe_allow_html=True)

