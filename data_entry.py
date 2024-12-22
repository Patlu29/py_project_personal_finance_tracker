import pandas as pd
import csv
from datetime import datetime 


class CSV:
    CSV_FILE = "finance_data.csv"
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
            
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
            df.to_csv(cls.CSV_FILE, index=False)
        
        @classmethod
        def add_entry(cls, date, amount, category, description):
            new_entry = {
                "Date": date,
                "Amount": amount,
                "Category": category,
                "Description": description
            }
        
         
CSV.initialize_csv()