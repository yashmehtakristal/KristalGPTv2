import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
from dotenv import load_dotenv
import os


DETA_KEY = st.secrets["DETA_KEY"]
deta = Deta(DETA_KEY)
db = deta.Base('Kristal_Detabase')


def insert_user(email, username, password):
    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """

    # Log the date when user was registered
    date_joined = str(datetime.datetime.now())

    # Store inserted object into database
    return db.put({'key': email, 'username': username, 'password': password, 'date_joined': date_joined})


def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """

    # db.fetch() retrieves a list of items matching a query.
    # It will retrieve everything if no query is provided, up to a limit of 1 MB or 1000 items.

    users = db.fetch()
    return users.items


def get_user_emails():
    """
    Fetch User Emails
    :return List of user emails:
    """
    
    users = db.fetch()
    emails = []

    # Accessing the items of the dictionary to get the "key" key (email attribute)
    for user in users.items:
        emails.append(user['key'])

    return emails


def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """

    users = db.fetch()
    usernames = []

    # Accessing the items of the dictionary to get the "username" key (username attribute)
    for user in users.items:
        usernames.append(user['username'])
    
    return usernames


def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """

    # In summary, it checks for the following:
    # Username can contain letters, digits, hyphens, or underscores.
    # Must be an '@' symbol
    # Domain name must consist of letters and/or digits
    # Must be a period (dot) separating the domain name from the TLD
    # The TLD must consist of one to three lowercase letters.

    pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True
    return False


def validate_username(username):
    """
    Checks Validity of username
    :param username:
    :return True if username is valid else False:
    """
    # In summary, this regex pattern is designed to validate strings that meet the following criteria:
    # The string can contain only alphanumeric characters (letters and digits).
    # The string can be empty (zero characters).

    pattern = "^[a-zA-Z0-9]+$"

    if re.match(pattern, username):
        return True
    
    return False


def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader('Sign Up')

        email = st.text_input('Email', placeholder='Enter Your Email',
                              help =
                              '''
                              Please make sure:
                              1) You enter a valid email
                              '''
                              )

        username = st.text_input('Username', placeholder='Enter Your Username', 
                                 help =
                                '''
                                Please make sure:
                                1) Username is at least 2 characters long
                                2) Username contains only alphanumeric characters (letters and digits)
                                '''
                                )

        password1 = st.text_input('Password', placeholder='Enter Your Password', type='password',
                                  help =
                                  '''
                                  Please make sure:
                                  1) Length of password is at least 6 characters long
                                  2) Password can contain any characters (letters, digits, underscore, dashes, period etc)
                                  '''
                                  )
        
        password2 = st.text_input('Confirm Password', placeholder='Confirm Your Password', type='password',
                                  help = "Please make sure the password inputted in this field is the same as password inputted in the above field"
                                  )

        if email:

            # If email string is according to expected format
            if validate_email(email):

                # If email not in current database
                if email not in get_user_emails():

                    # If username is according to expected format
                    if validate_username(username):

                        # If username not in current database
                        if username not in get_usernames():

                            # If length of username >= 2
                            # & length of password >= 6
                            if len(username) >= 2:
                                if len(password1) >= 6:

                                    # Check if password and confirm password fields are equal to each other
                                    if password1 == password2:
                                        
                                        # Hash the password using stauthenticator library
                                        hashed_password = stauth.Hasher([password2]).generate()

                                        # Add the email, username and hashed password corresponding to the user
                                        insert_user(email, username, hashed_password[0])

                                        st.success('Account created successfully!!')
                                        st.balloons()


                                    else:
                                        st.warning('Passwords Do Not Match')
                                else:
                                    st.warning('Password is too Short')
                            else:
                                st.warning('Username Too short - should be greater than 2 characters')
                        else:
                            st.warning('Username Already Exists')

                    else:
                        st.warning('Invalid Username')
                else:
                    st.warning('Email Already exists!!')
            else:
                st.warning('Invalid Email')

        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn1:
            st.form_submit_button('Sign Up')