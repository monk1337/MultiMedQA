import pandas as pd
import json
import random
import os

def read_json_(file):
    with open(file, 'r') as json_file:
        file_js = json.load(json_file)
    return file_js


def medmcqa(sample):
    template = f"Question: {sample['question']} \n(A) {sample['opa']} (B) {sample['opb']} (C) {sample['opc']} (D) {sample['opd']} \nAnswer:"
    return template

def medqa(sample):
    template = f"Question: {sample['question']} \n(A) {sample['option_A']} (B) {sample['option_B']} (C) {sample['option_C']} (D) {sample['option_D']} \nAnswer:"
    return template

def pubmedqa(sample):
    template = f"Answer the following question given the context (reply with one of the options): Context: {sample['context']} \n(A) Yes (B) No (C) Maybe \nAnswer:"
    return template

def mmlu(sample):
    template = f"Question: {sample['input']} \n(A) {sample['A']} (B) {sample['B']} (C) {sample['C']} (D) {sample['D']} \nAnswer:"
    return template

prompt_dict = {
                'pubmedqa' : './prompts/pubmedqa_fewshots.json',
                'medqa' : './prompts/medqa_fewshots.json',
                'medmcqa' : './prompts/medmcqa_fewshots.json', 
                'mmlu_anatomy': './prompts/mmlu_anatomy_fewshots.json',
                'mmlu_clinical': './prompts/mmlu_clinical_fewshots.json',
                'mmlu_professional_medicine': './prompts/mmlu_professional_medicine_fewshots.json',
                'mmlu_genetics': './prompts/mmlu_medical_genetics_fewshots.json',
                'mmlu_college_medicine': './prompts/mmlu_college_medicine_fewshots.json',
                'mmlu_college_biology': './prompts/mmlu_college_biology_fewshots.json',
    
}


func_dict = {
                'pubmedqa' : pubmedqa,
                'medqa' : medqa,
                'medmcqa' : medmcqa, 
                'mmlu_anatomy': mmlu,
                'mmlu_clinical': mmlu,
                'mmlu_professional_medicine': mmlu,
                'mmlu_genetics': mmlu,
                'mmlu_college_medicine': mmlu,
                'mmlu_college_biology': mmlu,
    
}

def select_prompt(list_of_prompts, n_samples, random_= False):
    if random_:
        return random.sample(list_of_prompts, n_samples)
    else:
        return list_of_prompts[:n_samples]


def prompt_data(dataset_name, n_shots, random_ = False):
    prompt    = read_json_(f"{prompt_dict[dataset_name]}")
    instruction = prompt['instruction']
    shots       = prompt['shots']
    shots_      = select_prompt(shots, n_shots, random_= random_)
    for single_shot in shots_:
        instruction+= f"\n\n{single_shot}"
    return instruction


def get_prompts(query, dataset_name, n_shots, random_):
    prompt_d = prompt_data(dataset_name, n_shots, random_ = random_)
    sample_  = func_dict[dataset_name](query)
    full_in = prompt_d + '\n\n' + sample_
    return full_in
