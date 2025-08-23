import pickle
import pandas as pd
import requests
import streamlit as st
from user_definition import *

def retrieve_data_from_urls(url_list: list) -> list:
    """
    Read data from url_list and return
    a list of unique dictionaries
    which includes all the data from url in url_list.
    """
    list1 = []
    for i in range(len(url_list)):
        response = requests.get(url_list[i])
        data = pickle.loads(response.content)
        list1.extend(data)
    return list1

def filter_by_company(data: pd.DataFrame, company_dictionary: dict)\
        -> pd.DataFrame:
    """
    For the given data (data frame) and company_dictionary,
    create checkboxes and return a new dataframe
    which only includes data being checked.
    """
    return

if __name__ == '__main__':
    pass