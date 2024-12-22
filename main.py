import pandas as pd
import csv
from datetime import datetime 
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    # create and name the scv file
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]
    FORMAT = "%d-%m-%Y"
    
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
        
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask]
        
        if filtered_df.empty:
            print("No transactions found in the given range")
        else:
            print(f"Transactions between {start_date.strftime(CSV.FORMAT)} and {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"Date": lambda x: x.strftime(CSV.FORMAT)}))
            
        total_income = filtered_df[filtered_df["category"] == "Income"]["Amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "Expense"]["Amount"].sum()
        
        print("\n Summary: ")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Net Savings: ${total_income - total_expense:.2f}")
        
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of transaction (dd-mm-yyyy) or press enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
        
add()