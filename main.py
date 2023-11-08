# Need to import pysqlite3 like this
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st

# Setting page config & header
st.set_page_config(page_title="Kristal Retriever", page_icon="📖", layout="wide", initial_sidebar_state="expanded")
st.header("📖 Kristal Retriever")

from streamlit_extras.app_logo import add_logo
from st_pages import Page, Section, add_page_title, show_pages, hide_pages
from database_helper_functions import sign_up, fetch_users
import streamlit_authenticator as stauth
import bcrypt


# Add the logo to the sidebar
add_logo("https://assets-global.website-files.com/614a9edd8139f5def3897a73/61960dbb839ce5fefe853138_Kristal%20Logotype%20Primary.svg")

show_pages(
    [
        Page("main.py","Login", "🗝️"),
        Page("pages/home.py", "About", "😀"),
        Page("pages/bulk_upload_basic.py", "Bulk Upload - Basic", "📚"),
        Page("pages/bulk_upload_advanced.py", "Bulk Upload - Advanced", "📚"),
        Page("pages/qa_basic.py", "Q&A - Basic", "❓"),
        Page("pages/qa_advanced.py", "Q&A - Advanced", "❓")
    ]
)

# Session state variables
if "logged_out" not in st.session_state:
    st.session_state.logged_out = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    hide_pages(["About", "Bulk Upload - Basic", "Bulk Upload - Advanced", "Q&A - Basic", "Q&A - Advanced"])

if st.session_state.logged_out:
    hide_pages(["About", "Bulk Upload - Basic", "Bulk Upload - Advanced", "Q&A - Basic", "Q&A - Advanced"])

if "username" not in st.session_state:
    st.session_state.username = ''

if "Authenticator" not in st.session_state:
    st.session_state.Authenticator = None

if "logout" not in st.session_state:
    st.session_state.logout = False


try:
    users = fetch_users()

    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name = 'Streamlit', key = 'abcdef', cookie_expiry_days = 0)
    st.session_state.Authenticator = Authenticator

    email, authentication_status, username = Authenticator.login('Login', 'main')
    with st.form(key='login', clear_on_submit=True):
        st.subheader('Login')

        username = st.text_input('Username', placeholder='Enter Your Username', help =
                        '''
                        Please make sure:
                        1) Username is at least 2 characters long
                        2) Username contains only alphanumeric characters (letters and digits)
                        '''
                        )
        
        password = st.text_input('Password', placeholder='Enter Your Password', type='password',
                            help =
                            '''
                            Please make sure:
                            1) Length of password is at least 6 characters long
                            2) Password can contain any characters (letters, digits, underscore, dashes, period etc)
                            '''
                            )
        
        info, info1 = st.columns(2)
        
        if username:
            if username in usernames:
                if password:

                    st.session_state.username = username
                    password_match = bcrypt.checkpw(password.encode(), credentials['usernames'][username]['password'].encode())

                    if password_match is True:
                        st.session_state.logged_in = True
                        st.session_state.logout = False

                        st.sidebar.subheader(f'Welcome {username}')
                        logout_button = Authenticator.logout('Log Out', 'sidebar')

                        if logout_button:
                            st.session_state.logged_out = True
                            st.session_state.logged_in = False


                    elif password_match is False:
                        with info:
                            st.error('Incorrect Password or username')

                else:
                    with info:
                        st.warning('Please enter the password field')

            else:
                with info:
                    st.warning('Username does not exist in database')

        else:
            with info:
                st.warning('Please enter the username field')


        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn1:
            st.form_submit_button('Login')

except:
    st.success('Refresh Page')

