from model import DemoModel
import os
import pandas as pd
import uuid

my_env_var = ""

import json

def read_json_file(file_path):
    """
    Opens and reads a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The contents of the JSON file as a Python data structure (usually a list or dictionary).
    """
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return None


dataset_dict = {
                'pubmedqa' : './datasets/pubmedqa_combined_data.json',
                'medqa' : './datasets/medqa_test.json',
                'medmcqa' : './datasets/medmcqa_val.json',
                'mmlu_anatomy': './datasets/mmlu_anatomy.json',
                'mmlu_clinical': './datasets/mmlu_clinical_knowledge.json',
                'mmlu_professional_medicine': './datasets/mmlu_professional_medicine.json',
                'mmlu_genetics': './datasets/mmlu_medical_genetics.json',
                'mmlu_college_medicine': './datasets/mmlu_college_medicine.json',
                'mmlu_college_biology': './datasets/mmlu_college_biology.json'}


for dataset_name, path_csv in dataset_dict.items():
    for shots_points in [0, 3, 5]:
        print("current dataset and task shot", dataset_name, path_csv, shots_points)
        data_dict = read_json_file(path_csv)
        model = DemoModel(f'shot_example_{shots_points}', dataset_name)
        model.start_generating(data_dict, dataset_name, shots_points, True)
