from datetime import datetime

date_format = "%d-%m-%Y"

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date Format.. Please enter a valid date in(dd-mm-yyyy) format")
        return get_date(prompt, allow_default)
    

def get_amount():
    pass

def get_categry():
    pass

def get_description():
    pass