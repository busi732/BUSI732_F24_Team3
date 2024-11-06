import pandas as pd
def read_data(data):
    """ Reads CSV data file and outputs a Pandas DataFrame"""
    df = pd.read_csv("../../data/raw/"+data)
    return df