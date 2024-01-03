import os
import pandas as pd
import json

def format_medmcqa(input_dict):
    # Extracting necessary information from the input dictionary
    question = input_dict['question']
    options = {
        'A': input_dict['opa'],
        'B': input_dict['opb'],
        'C': input_dict['opc'],
        'D': input_dict['opd']
    }
    # Directly map the 'cop' index (0-based) to the corresponding option value
    correct_answer_index = input_dict['cop']
    correct_answer_options = [input_dict['opa'], input_dict['opb'], input_dict['opc'], input_dict['opd']]
    correct_answer = correct_answer_options[correct_answer_index]

    # Format the explanation if it exists
    explanation = input_dict.get('exp', '')

    # Creating the new formatted dictionary
    new_format_dict = {
        'Question': question,
        'Options': options,
        'Correct Answer': correct_answer,
        'Explanation': explanation
    }
    return new_format_dict


def format_mmlu_medical_genetics(df, dataset_name):
    formatted_data = []
    for idx, row in df.iterrows():
        temp_dict = {}
        options_all = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        prompt_d     = {
            'Question': row['input'],
            'Options': options_all,
            'Correct Answer': options_all[row['target']],
            'Correct Option': row['target']
        }
        temp_dict['data'] = prompt_d
        temp_dict['id']       = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)
    return formatted_data


def format_medmcqa_val(df, dataset_name):
    formatted_data = []
    for idx, row in df.iterrows():

        temp_dict = {}
        options_  = {0: row['opa'], 1: row['opb'], 2: row['opc'], 3: row['opd']}
        options_alpha  = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
        
        
        prompt_d = {
            'Question': row['question'],
            'Options': {'A': row['opa'], 'B': row['opb'], 'C': row['opc'], 'D': row['opd']},
            'Correct Answer': options_[row['cop']],  # Assuming 'cop' column contains index (0-3) of the correct option
            'Correct Option': options_alpha[row['cop']],
            'Explanation' : str(row['exp']),
            'Subject_name': str(row['subject_name'])
        }

        temp_dict['data'] = prompt_d
        temp_dict['id']   = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)
    return formatted_data


def format_mmlu_professional_medicine(df, dataset_name):
    
    formatted_data = []
    for idx, row in df.iterrows():
        temp_dict = {}
        options_all = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        prompt_d     = {
            'Question': row['input'],
            'Options': options_all,
            'Correct Answer': options_all[row['target']],
            'Correct Option': row['target']
        }
        temp_dict['data'] = prompt_d
        temp_dict['id']       = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)

    return formatted_data


def format_mmlu_anatomy(df, dataset_name):
    formatted_data = []
    for idx, row in df.iterrows():
        temp_dict = {}
        options_all = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        prompt_d     = {
            'Question': row['input'],
            'Options': options_all,
            'Correct Answer': options_all[row['target']],
            'Correct Option': row['target']
        }
        temp_dict['data'] = prompt_d
        temp_dict['id']       = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)
    
    return formatted_data

def format_medqa_test(df, dataset_name):
    formatted_data = []
    for idx, row in df.iterrows():
        temp_dict = {}

        opentions = {'A': row['option_A'], 'B': row['option_B'], 'C': row['option_C'], 'D': row['option_D']}
        prompt_d   = {
            'Question': row['question'],
            'Options': opentions,
            'Correct Answer': opentions[row['answer_idx']],  # Assuming 'answer_idx' contains the index (A-D) of the correct option
            'Correct Option': row['answer_idx']
        }

        temp_dict['data']     = prompt_d
        temp_dict['id']       = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)
    return formatted_data

def format_mmlu_college_biology(df, dataset_name):
    formatted_data = []
    for idx, row in df.iterrows():
        temp_dict = {}
        options_all = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        prompt_d     = {
            'Question': row['input'],
            'Options': options_all,
            'Correct Answer': options_all[row['target']],
            'Correct Option': row['target']
        }
        temp_dict['data'] = prompt_d
        temp_dict['id']       = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)
    return formatted_data

def format_mmlu_college_medicine(df, dataset_name):
    formatted_data = []
    for idx, row in df.iterrows():
        temp_dict = {}
        options_all = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        prompt_d     = {
            'Question': row['input'],
            'Options': options_all,
            'Correct Answer': options_all[row['target']],
            'Correct Option': row['target']
        }
        temp_dict['data'] = prompt_d
        temp_dict['id']       = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)
    return formatted_data

def format_mmlu_clinical_knowledge(df, dataset_name):
    formatted_data = []
    for idx, row in df.iterrows():
        temp_dict = {}
        options_all = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        prompt_d     = {
            'Question': row['input'],
            'Options': options_all,
            'Correct Answer': options_all[row['target']],
            'Correct Option': row['target']
        }
        temp_dict['data'] = prompt_d
        temp_dict['id']       = row['id']
        temp_dict['dataset_name'] = dataset_name
        
        formatted_data.append(temp_dict)
    return formatted_data


formatting_functions = {
    'mmlu_medical_genetics.csv': format_mmlu_medical_genetics,
    'medmcqa_val.csv': format_medmcqa_val,
    'mmlu_professional_medicine.csv': format_mmlu_professional_medicine,
    'mmlu_anatomy.csv': format_mmlu_anatomy,
    'medqa_test.csv': format_medqa_test,
    'mmlu_college_biology.csv': format_mmlu_college_biology,
    'mmlu_college_medicine.csv': format_mmlu_college_medicine,
    'mmlu_clinical_knowledge.csv': format_mmlu_clinical_knowledge
}

import json

csv_files_directory = '.'
formatted_data_directory = 'formatted_data'

# Process and format each file using its respective function, and save as JSON
for filename, formatting_function in formatting_functions.items():
    if formatting_function is not None:
        
        # Constructing the full path for the input and output files
        input_file_path = os.path.join(csv_files_directory, filename)
        output_file_path = os.path.join(formatted_data_directory, f"formatted_{filename}.json")

        # Read the CSV file
        df = pd.read_csv(input_file_path)

        try:
        # Format the data using the respective function
            formatted_data = formatting_function(df, filename)
    
            # Save the formatted data as a JSON file
            with open(output_file_path, 'w') as json_file:
                json.dump(formatted_data, json_file, indent=4)
        except Exception as e:
            print(filename, formatting_function)
        
# Return the path of the directory containing the formatted files
formatted_data_directory
