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
advertising_file_path = 'advertising-data.xlsx'
event_data = pd.read_excel(event_file_path, sheet_name='Events')
newsletter_data = pd.read_excel(event_file_path, sheet_name='Newsletter')
advertising_data = pd.read_excel(advertising_file_path)

#Iterate through Registration Sheets
folder_path = './registration-sheets'

for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        excel_file_name = os.path.splitext(file_name)[0]
        registration_data = pd.read_excel(f"{folder_path}/{excel_file_name}.xlsx")
        event_name = excel_file_name.replace('-', ' ')
        # Dataframes available: event_data, newsletter_data and registration_data
        # Plotting Data: registration_data
        plt.figure(figsize=(10, 6))
        plt.plot(
                registration_data['Date-Created'],
                range(len(registration_data['Date-Created'])),
                marker=".",
                linestyle="-",
                color="blue",
                label="Registrations",
            )
        
        #Plotting Data: advertising_data
        event_advertising = advertising_data[advertising_data["Event"] == event_name]
        for ad_date in event_advertising["Dates"]:
            plt.axvline(x=ad_date, color="red", linestyle="--", label="Advertising Date")

        #Plotting Data: newsletter_data
        newsletter_dates = newsletter_data[newsletter_data["Event-Advertised"] == event_name]
        for date_value in newsletter_dates["Newsletter-Date"]:
            plt.axvline(x=date_value, color="purple", linestyle="--", label="Newsletter Advertised Date")

        # Customize the plot
        currentEvent = event_data[event_data["Event"] == event_name]
        #Plotting Data: Event Date
        for e in currentEvent["Date"]:
            plt.axvline(e, color="black", linestyle="-", label="Event Date")
        
        
        # RIGHT
        plt.title(f'{event_name} | {currentEvent["Modality"].values[0]} | Reg: {currentEvent["Registered"].values[0]} | Att: {currentEvent["Attended"].values[0]} | Rate: {currentEvent["Attended"].values[0] / currentEvent["Registered"].values[0]}')
        plt.xlabel('Date')
        plt.ylabel('# of Registrations')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Show plot
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()