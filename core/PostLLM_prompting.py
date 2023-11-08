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
from tenacity import retry, stop_after_attempt, wait_random_exponential

@st.cache_data(show_spinner = False)
def create_output_result_column(orignal_excel_file, llm_prompts_index, output_response):
    '''
    create_output_result_column: This function ultimately creates the "Output Result" column

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    llm_prompts_index: List of the index of the rows of prompts (in orignal_excel_file) that were fed to LLM
    output_response: List containing response of prompts passed to LLM

    Output -
    orignal_excel_file: Dataframe of the results excel file
    '''
    
    # Create new column "Output result" which adds the output prompts from list
    orignal_excel_file.loc[llm_prompts_index, 'Output result'] = output_response

    # Rearrange the columns so that 'Automatic Processed Input prompt' is in front of 'Manual Processed Input prompt'
    excel_columns = orignal_excel_file.columns.tolist()
    excel_columns.remove('Output result')  
    excel_columns.insert(excel_columns.index('Source Type'), 'Output result')
    orignal_excel_file = orignal_excel_file[excel_columns] 

    return orignal_excel_file


# @st.cache_data(show_spinner = False)
# @st.cache_resource(show_spinner = False)
def create_output_context_column(orignal_excel_file, llm_prompts_index, nodes_to_retrieve, output_context):
    '''
    create_output_context_column: This function ultimately creates the "Output Context" column

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    llm_prompts_index: List of the index of the rows of prompts (in orignal_excel_file) that were fed to LLM 
    nodes_to_retrieve: Number of nodes to retrieve from vector_retriever

    Output -
    orignal_excel_file: Dataframe of the results excel file
    '''

    new_output = orignal_excel_file.loc[llm_prompts_index, 'Field name']

    field_name_output_list = new_output.tolist()

    output_dict = dict(zip(field_name_output_list, output_context))

    output_prompt_context_value_list = []

    for key, value in output_dict.items():
        
        output_prompt_object = value

        combined_context = ""

        for i in range(nodes_to_retrieve):

            output_prompt_context_value = output_prompt_object.source_nodes[i].node.get_content()

            if combined_context:
                combined_context += '\n'
            
            combined_context += output_prompt_context_value

        # Append the combined context (of a single prompt) to the list
        output_prompt_context_value_list.append(combined_context)


    # Take each context and add appropriate line spacing if there is "\n" present
    for index, value in enumerate(output_prompt_context_value_list):

        lines = value.splitlines()

        result_string = '\n'.join(lines)

        output_prompt_context_value_list[index] = result_string

    orignal_excel_file.loc[llm_prompts_index, 'Output context'] = output_prompt_context_value_list

    return orignal_excel_file

@st.cache_data(show_spinner = False)
def intermediate_output_to_excel(orignal_excel_file, excel_directory, output_excel_filename, file_extension):
    '''
    intermediate_output_to_excel: This is an intermediary function outputting the excel file [Should stop here if you only want to fill the first document (FAF form)]

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    excel_directory: Directory storing excel files
    output_excel_filename: Excel file name that we will output
    file_extension: Extension of the file that we wish output file will be 

    Output - None
    '''
    output_excel_file = f"{output_excel_filename}.{file_extension}"
    excel_file_path = os.path.join(excel_directory, output_excel_file)
    orignal_excel_file.to_excel(excel_file_path, index=True)


