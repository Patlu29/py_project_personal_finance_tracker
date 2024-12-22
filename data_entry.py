import pandas as pd
import csv
from datetime import datetime 


class CSV:
    # create and name the scv file
    CSV_FILE = "finance_data.csv"
    
    # create a function to initialize a new csv file if it desn,t exist
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
            
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"]) # names of the data columns 
            df.to_csv(cls.CSV_FILE, index=False)# it convert dataframe into csv file
            
    # new class method for adding entry to the csv file    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        
         
CSV.initialize_csv()