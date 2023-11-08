#!/usr/bin/env python
# coding: utf-8

# All imports

import pandas as pd
import os
import time
import warnings
warnings.filterwarnings("ignore")
import streamlit as st


# @st.cache_resource(show_spinner = False)
@st.cache_data(show_spinner = False)
def create_filtered_excel_file(orignal_excel_file, llm_prompts_index):
    '''
    create_filtered_excel_file: This function will just create a new dataframe called filtered_excel_file (for safety) containing those prompts passed to LLM (Source Type = LLM, and not NA)

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    llm_prompts_index: List of the index of the rows of prompts (in orignal_excel_file) that were fed to LLM 

    Output - 
    filtered_excel_file: New dataframe containing those prompts passed to LLM (Source Type = LLM, and not NA)
    '''

    # Creating new filtered_excel_file for safety of the data, so far - this is based on llm_prompts_index (where Source Type == LLM AND Excluding NA in Input prompt)
    filtered_excel_file = orignal_excel_file.iloc[llm_prompts_index] 

    return filtered_excel_file



# Define a function to create 'Final Output result_cleaned' column
@st.cache_data(show_spinner = False)
def create_final_output_result_cleaned_column(row):
    '''
    create_final_output_result_cleaned_column: This function will extract the value of the corresponding key, if it is equal to field name

    Input:
    row - Each row of the filtered_excel_file dataframe (containing llm_prompts_index only)

    Output:
    For that particular row, it will provide the value in the final_output_result_cleaned column
    '''
    
    field_name = row['Field name']
    final_output = row["Final Output result"]
    extracted_values = []
    
    if final_output:

        if isinstance(final_output, list):

            for dictionary in final_output:
                if field_name in dictionary:
                    extracted_values.append(dictionary[field_name])

        elif isinstance(final_output, dict):
            if field_name in final_output:
                extracted_values.append(final_output[field_name])
            
    if extracted_values:
        return extracted_values[0]
    
    return None

# @st.cache_resource(show_spinner = False)
@st.cache_data(show_spinner = False)
def final_result_orignal_excel_file(filtered_excel_file, orignal_excel_file, llm_prompts_index):
    '''
    final_result_orignal_excel_file: This function will simply call previous function, copy the column (Final Output result_cleaned) to orignal_excel_file 

    Input:
    filtered_excel_file: New dataframe containing those prompts passed to LLM (Source Type = LLM, and not NA)

    Output:
    Orignal_excel_file: Dataframe of the results excel file (with the newly added 'Final Output result_cleaned' column)
    '''

    # Apply the function (create_final_output_result_cleaned_column) to each row (axis = 1) and store in a new column, 'Final Output result_cleaned'
    filtered_excel_file['Final Output result_cleaned'] = filtered_excel_file.apply(create_final_output_result_cleaned_column, axis=1)

    # Update orignal_excel_file for specific indexes according to filtered_excel_file
    orignal_excel_file.loc[llm_prompts_index, 'Final Output result_cleaned'] = filtered_excel_file['Final Output result_cleaned']

    return orignal_excel_file



@st.cache_data(show_spinner = False)
def reordering_columns(orignal_excel_file):
    '''
    reordering_columns: This function will reorder columns of orignal_excel_file according to the columns  

    Input:
    filtered_excel_file: New dataframe containing those prompts passed to LLM (Source Type = LLM, and not NA)

    Output:
    Orignal_excel_file: Dataframe of the results excel file (with the newly added 'Final Output result_cleaned' column)
    '''

    # Defining new column order of dataframe
    new_column_order = ['Field name', 'Data Type', 'Input prompt', 'Source Type', 'Variable replace', 'Automatic Processed Input prompt', 'Output context', 'Output result', 'Final Output result', 'Final Output result_cleaned']

    # Renaming columns
    orignal_excel_file = orignal_excel_file[new_column_order]

    return orignal_excel_file
    


