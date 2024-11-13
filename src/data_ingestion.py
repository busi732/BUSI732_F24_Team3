import pandas as pd

def data_ingestion(fileName: str, colName: str, format: str):
  
  """
    Loads a CSV file and converts a specified column to datetime format.

    Parameters:
    ----------
    filename : str
        The path to the CSV file to load. This file should contain a column
        that needs conversion to datetime format.
        
    colname : str
        The name of the column within the CSV file to be converted into
        datetime format. The column should contain data that can be parsed
        as dates.

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with the specified column converted to datetime format.
    """
  
  # Path to the raw data
  DATA_PATH = "../data/raw/"

  # reading the csv file
  df = pd.read_csv(DATA_PATH+fileName)
  
  # scada/fault one goes to minutes one goes to seconds, ignore all seconds to keep all minutes
  df[colName] = pd.to_datetime(df[colName], format=format).dt.floor('min')
  return df

