import os
import requests
from datetime import datetime
import pandas as pd
from tkinter import messagebox

API_KEY = os.environ.get('API_KEY_CURR_CONV')
API_URL_CONVERTER = "https://api.freecurrencyapi.com/v1/latest/"

CURRENCIES = "currencies.csv"
CONVERSION_RATES = "conversion_rates.csv"
LAST_TIME_FILE = "last_updated.txt"

params = {
    "apikey": API_KEY
}

def write_time(time:datetime):
    with open(LAST_TIME_FILE, "wt") as last_time:
        last_time.write(time.isoformat())

def check_get_data():
    now = datetime.now()

    with open(LAST_TIME_FILE, "rt") as last_time:
        time = last_time.readline()
        if time != "":
            date = datetime.fromisoformat(time)
            if (date - now).days + 1 < 0:
                write_time(now)
                return True
            else:
                return False
        else:
            write_time(now)
            return True
        
def write_data(data:dict):
    new_dict = {
        "Currency": [],
        "Rate": []
    }

    for (key, value) in data.items():
        new_dict["Currency"].append(key)
        new_dict["Rate"].append(value)

    df = pd.DataFrame(data=new_dict)
    df.to_csv(path_or_buf=CONVERSION_RATES)
        
def get_data():
    if check_get_data() is True:
        messagebox.showinfo(title="Getting Data...", message="Data is being retrieved. Program will start shortly!")

        with requests.get(API_URL_CONVERTER, params=params) as connection:
            connection.raise_for_status()
            response = connection.json()
        write_data(response["data"])
        return response["data"]
    else:
        data = {}
        df = pd.read_csv(CONVERSION_RATES)
        for (curr, rate) in zip(df['Currency'], df['Rate']):
            data[curr] = rate
        return data
    
def get_currency_names():
    curr_names = {}
    df = pd.read_csv(CURRENCIES)

    for (name, code) in zip(df["Name"], df["Code"]):
        curr_names[name] = code
    return curr_names
