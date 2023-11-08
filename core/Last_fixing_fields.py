#!/usr/bin/env python
# coding: utf-8

# All imports
import streamlit as st
import pandas as pd
import os
import time
import warnings
warnings.filterwarnings("ignore")


@st.cache_data(show_spinner = False)
def find_result_fund_name(orignal_excel_file):
    '''
    find_result_fund_name: This function will find the value from 'Final Output result_cleaned' column where field name is fund name.

    Input - 
    orignal_excel_file: Dataframe of the results excel file

    Output - 
    results_fund_name_value: Variable containing fund name
    '''

    result_fund_name = orignal_excel_file[orignal_excel_file['Field name'] == 'Fund Name']

    if not result_fund_name.empty:

        series_output = result_fund_name['Final Output result_cleaned']
        results_fund_name_value = series_output.str.cat(sep=' ')

    return results_fund_name_value


@st.cache_data(show_spinner = False)
def find_result_fund_house(orignal_excel_file):
    '''
    find_result_fund_house: This function will find the value from 'Final Output result_cleaned' column where field name is fund house.

    Input - 
    orignal_excel_file: Dataframe of the results excel file

    Output - 
    results_fund_house_value: Variable containing fund house
    '''

    result_fund_house = orignal_excel_file[orignal_excel_file['Field name'] == 'Fund House']

    if not result_fund_house.empty:
        
        series_output = result_fund_house['Final Output result_cleaned']

        result_fund_house_value = series_output.str.cat(sep=' ')

    return result_fund_house_value

@st.cache_data(show_spinner = False)
def find_result_fund_class(orignal_excel_file):
    '''
    find_result_fund_class: This function will find the value from 'Final Output result_cleaned' column where field name is fund class.

    Input - 
    orignal_excel_file: Dataframe of the results excel file

    Output - 
    result_fund_class_value: Variable containing fund class
    '''

    result_class = orignal_excel_file[orignal_excel_file['Field name'] == 'Class']

    if not result_class.empty:
        
        series_output = result_class['Final Output result_cleaned']

        result_fund_class_value = series_output.str.cat(sep=' ')

    return result_fund_class_value

@st.cache_data(show_spinner = False)
def find_result_currency(orignal_excel_file):
    '''
    find_result_currency: This function will find the value from 'Final Output result_cleaned' column where field name is currency.

    Input - 
    orignal_excel_file: Dataframe of the results excel file

    Output - 
    result_currency_value: Variable containing currency
    '''

    result_currency = orignal_excel_file[orignal_excel_file['Field name'] == 'Currency']

    if not result_currency.empty:
        
        series_output = result_currency['Final Output result_cleaned']
        result_currency_value = series_output.str.cat(sep=' ')

    return result_currency_value


@st.cache_data(show_spinner = False)
def find_result_acc_or_inc(orignal_excel_file):

    '''
    find_result_currency: This function will find the value from 'Final Output result_cleaned' column where field name is "acc or inc".

    Input - 
    orignal_excel_file: Dataframe of the results excel file

    Output - 
    result_acc_or_inc: Variable containing acc or inc
    '''

    result_acc_or_inc = orignal_excel_file[orignal_excel_file['Field name'] == 'Acc or Inc']

    if not result_acc_or_inc.empty:
        
        series_output = result_acc_or_inc['Final Output result_cleaned']
        result_acc_or_inc_value = series_output.str.cat(sep=' ')

    return result_acc_or_inc_value


@st.cache_data(show_spinner = False)
def create_new_kristal_alias(results_fund_name_value, result_fund_house_value, result_fund_class_value, result_currency_value, result_acc_or_inc_value):
    '''
    create_new_kristal_alias: Create kristal alias by concatenating all the variables names.

    Input - 
    results_fund_name_value: Variable containing string of fund name
    result_fund_house_value: Variable containing string of fund house
    result_fund_class_value: Variable containing string of fund class 
    result_currency_value: Variable containing string of currency
    result_acc_or_inc_value: Variable containing string of "acc or inc" value

    Output - 
    kristal_alias: Variable containing concatenated kristal alias
    '''

    kristal_alias = f"{result_fund_house_value} {results_fund_name_value} - {result_fund_class_value} ({result_currency_value}) {result_acc_or_inc_value}"

    return kristal_alias


@st.cache_data(show_spinner = False)
def update_kristal_alias(orignal_excel_file, kristal_alias):
    '''
    update_kristal_alias: Function for updating the kristal alias value in the orignal_excel_file dataframe

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    kristal_alias: Variable containing updated kristal alias

    Output - 
    orignal_excel_file: Dataframe of the results excel file (with updated kristal alias value)
    '''
    index_kristal_alias = orignal_excel_file.index[orignal_excel_file['Field name'] == 'Kristal Alias'].tolist()
    orignal_excel_file.loc[index_kristal_alias, "Final Output result_cleaned"] = kristal_alias

    return orignal_excel_file



@st.cache_data(show_spinner = False)
def update_sponsored_by(orignal_excel_file, sponsored_by):
    '''
    update_sponsored_by: Function for updating the kristal alias value in the orignal_excel_file dataframe

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    sponsored_by: Variable containing updated sponsored by value

    Output - 
    orignal_excel_file: Dataframe of the results excel file (with updated sponsored by value)
    '''

    index_sponsored_by = orignal_excel_file.index[orignal_excel_file['Field name'] == 'Sponsored By'].tolist()
    orignal_excel_file.loc[index_sponsored_by, "Final Output result_cleaned"] = sponsored_by

    return orignal_excel_file



@st.cache_data(show_spinner = False)
def update_required_broker(orignal_excel_file, required_broker):
    '''
    update_required_broker: Function for updating the kristal alias value in the orignal_excel_file dataframe

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    required_broker: Variable containing updated required broker value

    Output - 
    orignal_excel_file: Dataframe of the results excel file (with updated required broker value)
    '''

    index_required_broker = orignal_excel_file.index[orignal_excel_file['Field name'] == 'Required Broker'].tolist()
    orignal_excel_file.loc[index_required_broker, "Final Output result_cleaned"] = required_broker

    return orignal_excel_file


@st.cache_data(show_spinner = False)
def update_transactional_fund(orignal_excel_file, transactional_fund):
    '''
    update_transactional_fund: Function for updating the kristal alias value in the orignal_excel_file dataframe

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    required_broker: Variable containing updated required broker value

    Output - 
    orignal_excel_file: Dataframe of the results excel file (with updated required broker value)
    '''

    index_transactional_fund = orignal_excel_file.index[orignal_excel_file['Field name'] == 'Transactional Fund'].tolist()
    orignal_excel_file.loc[index_transactional_fund, "Final Output result_cleaned"] = transactional_fund

    return orignal_excel_file


@st.cache_data(show_spinner = False)
def update_disclaimer(orignal_excel_file, disclaimer):
    '''
    update_disclaimer: Function for updating the disclaimer in the orignal_excel_file dataframe

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    transactional_fund: Variable containing updated required broker value

    Output - 
    orignal_excel_file: Dataframe of the results excel file (with updated required broker value)
    '''

    index_result_disclaimer = orignal_excel_file.index[orignal_excel_file['Field name'] == 'Disclaimer'].tolist()
    orignal_excel_file.loc[index_result_disclaimer, "Final Output result_cleaned"] = disclaimer

    return orignal_excel_file

@st.cache_data(show_spinner = False)
def update_risk_disclaimer(orignal_excel_file, risk_disclaimer):
    '''
    update_risk_disclaimer: Function for updating the risk disclaimer in the orignal_excel_file dataframe

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    transactional_fund: Variable containing updated required broker value

    Output - 
    orignal_excel_file: Dataframe of the results excel file (with updated required broker value)
    '''

    index_kristal_risk_disclaimer = orignal_excel_file.index[orignal_excel_file['Field name'] == 'Risk Disclaimer'].tolist()
    orignal_excel_file.loc[index_kristal_risk_disclaimer, "Final Output result_cleaned"] = risk_disclaimer

    return orignal_excel_file


@st.cache_data(show_spinner = False)
def find_nav_value(orignal_excel_file):
    '''
    find_nav_value: Function to find NAV value in "Final Output result_cleaned" where "Field name" is "NAV"

    Input - 
    orignal_excel_file: Dataframe of the results excel file

    Output - 
    result_nav_value: Value where 'Field Name' contains 'NAV'
    '''

    try: 
        # Find rows where 'Field Name' contains 'NAV'
        result_nav_row = orignal_excel_file[orignal_excel_file['Field name'] == 'NAV']

        # Set result_nav_value variable
        result_nav_value = result_nav_row["Final Output result_cleaned"].iloc[0]

    except:
        # Handle the case where the 'Field name' column doesn't exist in the DataFrame
        result_nav_value = None  # You can set it to None or any other default value

    return result_nav_value


@st.cache_data(show_spinner = False)
def update_nav_value(orignal_excel_file, result_nav_value):
    '''
    update_nav_value: Function to update NAV value in "Final Output result_cleaned" where "Field name" is "Default NAV"

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    result_nav_value: Value where 'Field Name' contains 'NAV'

    Output - 
    orignal_excel_file: Dataframe of the results excel file (updated with the NAV value)
    '''

    # Find rows where 'Field Name' contains 'Default NAV'
    index_default_nav = orignal_excel_file.index[orignal_excel_file['Field name'] == 'Default NAV'].tolist()

    # Output default_nav_value to "Final Output result_cleaned"
    orignal_excel_file.loc[index_default_nav, "Final Output result_cleaned"] = result_nav_value

    return orignal_excel_file
