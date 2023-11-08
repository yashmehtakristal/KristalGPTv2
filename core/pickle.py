#!/usr/bin/env python
# coding: utf-8

# All imports
import streamlit as st
import pickle
import pandas as pd
import os
import time
import warnings
warnings.filterwarnings("ignore")



# Save to pickle file
def save_to_pickle(directory_pickles, table_dfs):
    '''
    save_to_pickle:  
    Explanation: Save the table_dfs into a pickle file (for easy saving and loading)

    Input - 
    directory_pickles: the directory/folder to where our files are stored

    Output - 
    table_dfs: list containing dataframe of various tables
    '''

    # Open the file in binary write mode ('wb') and save the list
    with open(directory_pickles, 'wb') as file:
        
        # Dump the list into a pickle object
        pickle.dump(table_dfs, file)

    return directory_pickles


# Load from pickle file
@st.cache_data(show_spinner = False)
def load_from_pickle(directory_pickles):
    '''
    load_from_pickle:  
    Explanation: This will load the pickle file 

    Input - 
    directory_pickles: the directory/folder to where our files are stored

    Output - 
    table_dfs: list containing dataframe of various tables
    '''

    # Load the DataFrame from the pickle file
    table_dfs = pd.read_pickle(directory_pickles)

    return table_dfs



