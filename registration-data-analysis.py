import pandas as pd
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
