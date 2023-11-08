### Functions we can call


docs = read_documents_from_directory(directory = "Documents") # Call read_documents function
table_dfs = iterate_files_from_directory(directory = "Documents") # Call iterate_files_directory function


directory_pickles = save_to_pickle(directory_pickles = "Pickle/table_dfs.pkl", table_dfs = table_dfs) # Call function to save the table_dfs to pickle file
# table_dfs = load_from_pickle(directory_pickles = "Pickle/table_dfs.pkl") # Call function to load from pickle file - Uncomment this code if you want to load from pickle file


llm, service_context, df_query_engines = query_engine(table_dfs = table_dfs) # Calling query_engine function
vector_index, vector_retriever, df_id_query_engine_mapping, nodes_to_retrieve = build_vector_index(service_context = service_context, df_query_engines = df_query_engines, docs = docs, nodes_to_retrieve = 3) # Calling build_vector_index function





orignal_excel_file, info_excel_file = iterate_files(excel_directory = "Results", input_excel_file = "results", file_extension = "xlsx") # Call iterate_files function for directory results, input file results and xlsx file extension
LLM_inputs, Discretionary_inputs = conditions_excel(orignal_excel_file) # Call conditions_excel function 
fund_variable = extract_fund_variable(info_excel_file = info_excel_file) # Call extract_fund_variable function to obtain fund variable
orignal_excel_file, llm_full_index = prompts_to_substitute_variable(orignal_excel_file = orignal_excel_file, fund_variable = fund_variable, LLM_inputs = LLM_inputs) # Call function to run prompts_to_substitute_variable function
orignal_excel_file, llm_prompts_to_use, llm_prompts_index = storing_input_prompt_in_list(orignal_excel_file = orignal_excel_file, llm_full_index = llm_full_index) # Calling storing_input_prompt_in_list function to get prompts in list format


recursive_retriever, response_synthesizer, query_engine = recursive_retriever(orignal_excel_file = orignal_excel_file, vector_retriever = vector_retriever, df_id_query_engine_mapping = df_id_query_engine_mapping, service_context = service_context) # Calling recursive retriever function


# output_response, output_context = individual_prompt(query_engine = query_engine, prompt = "Please give me a short summary of this document") # Call individual_prompt function
output_response, output_context = prompt_loop(query_engine = query_engine, llm_prompts_to_use = llm_prompts_to_use) # Call prompt_loop function


orignal_excel_file = create_output_result_column(orignal_excel_file = orignal_excel_file, llm_prompts_index = llm_prompts_index, output_response = output_response) # Call function to create output result column
orignal_excel_file = create_output_context_column(orignal_excel_file, llm_prompts_index, nodes_to_retrieve = nodes_to_retrieve) # Call create_output_context_column function
intermediate_output_to_excel(orignal_excel_file = orignal_excel_file, excel_directory = "Results", output_excel_filename = "results_output", file_extension = "xlsx") # Call function output_files for directory results, input file results and xlsx file extension


schema = create_schema_from_excel(orignal_excel_file, llm_prompts_index) # Call function create_schema_from_excel
orignal_excel_file = parse_value(output_response = output_response, llm_prompts_index = llm_prompts_index) # Call function parse_value


filtered_excel_file = create_filtered_excel_file(orignal_excel_file = orignal_excel_file, llm_prompts_index = llm_prompts_index) # Calling create_filtered_excel_file function
orignal_excel_file = final_result_orignal_excel_file(filtered_excel_file = filtered_excel_file) # Call final_result_orignal_excel_file function
orignal_excel_file = reordering_columns(orignal_excel_file) # Call reordering_columns function 


results_fund_name_value = find_result_fund_name(orignal_excel_file) # Calling find_result_fund_name function to find fund name
result_fund_house_value = find_result_fund_house(orignal_excel_file) # Calling find_result_fund_house function to find fund house
result_fund_class_value = find_result_fund_class(orignal_excel_file) # Calling find_result_fund_class function to find fund class
result_currency_value = find_result_currency(orignal_excel_file) # Calling find_result_currency function to find currency value
result_acc_or_inc_value = find_result_acc_or_inc(orignal_excel_file) # Calling find_result_acc_or_inc function to find acc/inc value
kristal_alias = create_new_kristal_alias(results_fund_name_value, result_fund_house_value, result_fund_class_value, result_currency_value, result_acc_or_inc_value) # Storing kristal_alias variable
orignal_excel_file = update_kristal_alias(orignal_excel_file = orignal_excel_file, kristal_alias = kristal_alias) # Calling update_kristal_alias function to update orignal_excel_file
orignal_excel_file = update_sponsored_by(orignal_excel_file = orignal_excel_file, sponsored_by = "backend-staging+hedgefunds@kristal.ai") # Calling update_sponsored_by function to update orignal_excel_file
orignal_excel_file = update_required_broker(orignal_excel_file = orignal_excel_file, required_broker = "Kristal Pooled") # Calling update_sponsored_by function to update orignal_excel_file
orignal_excel_file = update_transactional_fund(orignal_excel_file = orignal_excel_file, transactional_fund = "Yes") # Calling update_transactional_fund function to update orignal_excel_file
orignal_excel_file = update_disclaimer(orignal_excel_file = orignal_excel_file,
    disclaimer = '''
    The recommendations contained herein are for the exclusive use of investor and prohibits any form of disclosure or reproduction. The content cannot be relied upon by any other person for any other purpose. The recommendations are preliminary information to the investors, are subject to risks and may change based on investment objectives, financials, liabilities or the risk profile of an investor. Any recommendations including financial advice provided by Kristal.AI or its affiliates shall be subject to contractual understanding, necessary documentation, applicable laws, approvals and regulations. The recommendations contained herein may not be eligible for sale/purchase in some jurisdictions, in specific, are not intended for residents of the USA or within the USA.Though the recommendations are based on information obtained from reliable sources and are provided in good faith, they may be valid only on the date and time the recommendations are provided and shall be subject to change without notice. Kristal.AI
    ''' 
    ) # Calling update_disclaimer function to update orignal_excel_file
orignal_excel_file = update_risk_disclaimer(orignal_excel_file = orignal_excel_file,
    result_kristal_risk_disclaimer = '''
    The recommendations contained herein are for the exclusive use of investor and prohibits any form of disclosure or reproduction. The content cannot be relied upon by any other person for any other purpose. The recommendations are preliminary information to the investors, are subject to risks and may change based on investment objectives, financials, liabilities or the risk profile of an investor. Any recommendations including financial advice provided by Kristal.AI or its affiliates shall be subject to contractual understanding, necessary documentation, applicable laws, approvals and regulations. The recommendations contained herein may not be eligible for sale/purchase in some jurisdictions, in specific, are not intended for residents of the USA or within the USA.Though the recommendations are based on information obtained from reliable sources and are provided in good faith, they may be valid only on the date and time the recommendations are provided and shall be subject to change without notice. Kristal.AI
    '''
    ) # Calling update_risk_disclaimer function to update orignal_excel_file
result_nav_value = find_nav_value(orignal_excel_file) # Call function find_nav_value to find NAV value
orignal_excel_file = update_nav_value(orignal_excel_file = orignal_excel_file, result_nav_value = result_nav_value) # Call function update_nav_value to update NAV value


output_to_excel(orignal_excel_file = orignal_excel_file, excel_directory = "Results", output_excel_filename = "results_output", file_extension = "xlsx") # Call function output_files for directory results, input file results and xlsx file extension
