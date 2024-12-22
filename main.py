import pandas as pd
import csv
from datetime import datetime 
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    # create and name the scv file
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]
    
    # create a function to initialize a new csv file if it desn,t exist
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
            
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS) # names of the data columns 
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
        # open a csv file in append mode("a") and newline for make a new line and clean the code
        with open(cls.CSV_FILE, mode="a", newline="") as csvfile:
            # it write a new fieldnames in the csv file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            # it write a new row with a new entry in the csv file
            writer.writerow(new_entry)
        print("Entry added successfully")
        
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of transaction (dd-mm-yyyy) or press enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
        
add()