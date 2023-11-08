#!/usr/bin/env python
# coding: utf-8


# All imports
# pdf imports
import streamlit as st
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.retrievers import RecursiveRetriever
from llama_index.retrievers import RecursiveRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response_synthesizers import get_response_synthesizer


# Other library imports
import pandas as pd
import time
from typing import Any, List, Optional


# @st.cache_data(show_spinner = False)
@st.cache_resource(show_spinner = False)
def recursive_retriever(orignal_excel_file, vector_retriever, df_id_query_engine_mapping, service_context, llm_prompts_to_use):
    '''
    recursive_retriever: This function uses recursive retriever in our RetrieverQueryEngine
    Operates in a for loop over all the prompts

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    vector_retriever: Top 3 nodes of vector index
    df_id_query_engine_mapping: Mapping of the query engine with each dataframe
    service_context: service_context object defined above

    Output -
    recursive_retriever: Instance of RecursiveRetriever class
    response_synthesizer: Output of get_response_synthesizer
    query_engine: Instance of Retriever Query Engine class
    '''

    recursive_retriever = RecursiveRetriever(
    "vector", 
    retriever_dict={"vector": vector_retriever}, 
    query_engine_dict = df_id_query_engine_mapping, 
    verbose = False,
    )

    response_synthesizer = get_response_synthesizer(
        service_context=service_context, 
        response_mode="no_text"
    )    

    query_engine = RetrieverQueryEngine.from_args(
        recursive_retriever, response_synthesizer = response_synthesizer
    )

    output_response = []
    output_context = []
    count = 1

    for prompt in llm_prompts_to_use:

        # Diagnostic purposes
        st.write(f"{count} time entering loop")

        # Diagnostic purposes - Checking prompt
        st.write(f"Prompt used for this iteration is {prompt}")

        # Diagnostic purposes - Query Engine
        # st.write(type(query_engine))
        # st.write(query_engine)  
        
        # Calling query engine 
        response = query_engine.query(f"{prompt}")

        # Appending to list
        output_context.append(response)
        output_response.append(response.response)
        #output_response.append(str(response))
        
        count += 1

        # Diagnostic purposes - response from LLM
        st.write(f"Response from llm is {response.response}")

        # Diagnostic purposes - context from LLM
        st.write(f"Context from LLM is {response}")

        
        # Wait 8 seconds before executing next prompt
        time.sleep(10)

    return output_response, output_context



# @st.cache_data(show_spinner = False)
# @st.cache_resource(show_spinner = False)
def recursive_retriever_old(vector_retriever, df_id_query_engine_mapping, service_context):
    '''
    recursive_retriever_old: This function uses recursive retriever in our RetrieverQueryEngine
    This function works good for 1 prompt only

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    vector_retriever: Top 3 nodes of vector index
    df_id_query_engine_mapping: Mapping of the query engine with each dataframe
    service_context: service_context object defined above

    Output -
    recursive_retriever: Instance of RecursiveRetriever class
    response_synthesizer: Output of get_response_synthesizer
    query_engine: Instance of Retriever Query Engine class
    '''

    recursive_retriever = RecursiveRetriever(
    "vector", 
    retriever_dict={"vector": vector_retriever}, 
    query_engine_dict = df_id_query_engine_mapping, 
    verbose = True,
    )

    response_synthesizer = get_response_synthesizer(
        service_context=service_context, 
        response_mode="compact"
    )    

    query_engine = RetrieverQueryEngine.from_args(
        recursive_retriever, response_synthesizer = response_synthesizer, verbose = True
    )


    return recursive_retriever, response_synthesizer, query_engine


# @st.cache_data(show_spinner = False)
@st.cache_resource(show_spinner = False)
def recursive_retriever_orignal(orignal_excel_file, vector_retriever, df_id_query_engine_mapping, service_context):
    '''
    Orignal recursive_retriever function. Here, the r
    recursive_retriever: This function uses recursive retriever in our RetrieverQueryEngine

    Input - 
    orignal_excel_file: Dataframe of the results excel file
    vector_retriever: Top 3 nodes of vector index
    df_id_query_engine_mapping: Mapping of the query engine with each dataframe
    service_context: service_context object defined above

    Output -
    recursive_retriever: Instance of RecursiveRetriever class
    response_synthesizer: Output of get_response_synthesizer
    query_engine: Instance of Retriever Query Engine class
    '''

    recursive_retriever = RecursiveRetriever(
    "vector", 
    retriever_dict={"vector": vector_retriever}, 
    query_engine_dict = df_id_query_engine_mapping, 
    verbose = False,
    )

    response_synthesizer = get_response_synthesizer(
        service_context=service_context, 
        response_mode="no_text"
    )    

    query_engine = RetrieverQueryEngine.from_args(
        recursive_retriever, response_synthesizer = response_synthesizer
    )


    return recursive_retriever, response_synthesizer, query_engine

