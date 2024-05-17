import time
import streamlit as st


class SignInUp:
    def __init__(self):
        super().__init__()
        from serverManagement import register_user, get_user_data, find_user_data
        r1 = st.container()
        with r1:
            st.markdown(
                "<p style='font-size: 3em; font-family: fantasy; text-align: center; color: #6E75A8'>INVENTORY MANAGEMENT SYSTEM</p>",
                unsafe_allow_html=True)
            st.markdown("")
            # st.markdown("")

        login_tab, signup_tab = st.tabs(["LOG IN", "REGISTER"])

        with login_tab:
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            login_button = st.button("LOG IN", key="login")
            st.markdown("""
                            <style>
                                div.stButton > button:first-child {
                                    background-color: #6E75A8;
                                    color: #ffffff;
                                    border-color: #6E75A8;
                                    width: 10em;
                                    height: 3em;
                                    margin-left: 15.5em;
                                }
                                div.stButton > button:first-child:hover {
                                    background-color: #B9C2FF;
                                    border-color: #B9C2FF;
                                }
                            </style>""", unsafe_allow_html=True)

            if login_button:
                user_data = find_user_data(email)
                if user_data != None and email == user_data['mail'] and password == user_data['password']:
                    st.session_state.username = user_data["name"]
                    st.session_state.id = user_data["id"]
                    st.session_state.admin = user_data["admin"]
                    st.success("LogIn successful")
                    time.sleep(2)
                    st.switch_page("pages/sales.py")
                else:
                    st.error("Wrong Credentials! please check and try again")


        with signup_tab:
            mail_sign_up = st.text_input("Email", key="signup_mail")
            username_sign_up = st.text_input("Username", key="signup_username")
            id_sign_up = st.text_input("ID", key="signup_id")
            password_sign_up = st.text_input("Password", type="password", key="signup_password")
            confirm_password_sign_up = st.text_input("Confirm Password", type="password", key="confirm_signup_password")
            signup_button = st.button("SIGN UP", key="signup")
            st.markdown("""
                            <style>
                                div.stButton > button:first-child {
                                    background-color: #6E75A8;
                                    color: #ffffff;
                                    border-color: #6E75A8;
                                    width: 10em;
                                    height: 3em;
                                    margin-left: 15.5em;
                                }
                                div.stButton > button:first-child:hover {
                                    background-color: #B9C2FF;
                                    border-color: #B9C2FF;
                                }
                            </style>""", unsafe_allow_html=True)
            if signup_button:
                check_user_data = find_user_data(mail_sign_up)
                if check_user_data == None:
                    if password_sign_up == confirm_password_sign_up:
                        register_user(mail_sign_up, username_sign_up, password_sign_up, id_sign_up)
                        st.success("Registration complete, Now you can LogIn into your account.")
                    else:
                        st.error("Password didn't match, please check and try again.")
                else:
                    st.error("This email is already registered!")
