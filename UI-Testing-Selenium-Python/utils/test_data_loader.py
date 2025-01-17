# test_data_loader.py
import json
import os

def load_test_data(file_name):
    with open(os.path.join(os.path.dirname(__file__), '../data', file_name), 'r') as file:
        return json.load(file)
