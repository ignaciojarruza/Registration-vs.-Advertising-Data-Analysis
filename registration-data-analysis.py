import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

class Event:
    def __init__(self, name, registered, attended, modality):
        self.name = name
        self.registered = registered
        self.attended = attended
        self.modality = modality

    def __str__(self):
        return f"{self.registered} | {self.attended}"
    
# Event Dataframe Gathering
event_file_path = 'registration-data.xlsx'
event_data = pd.read_excel(event_file_path, sheet_name='Events')
newsletter_data = pd.read_excel(event_file_path, sheet_name='Newsletter')

#Iterate through Registration Sheets
folder_path = './registration-sheets'

for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        excel_file_name = os.path.splitext(file_name)[0]
        event_name = excel_file_name.replace('-', ' ')
        print(event_name)