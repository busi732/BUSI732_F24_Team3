import pandas as pd

def read_data(data):
    """ Reads CSV data file and outputs a Pandas DataFrame"""
    
    # Going back to the main folder and then navigativing to the data and raw to import the dataset.
    df = pd.read_csv("../data/raw/"+data)
    return df


def process_raw_data():
    
    fault_df = read_data("fault_data.csv")   # importing fault dataset
    scada_df = read_data("scada_data.csv")   # importing scada dataset
    status_df = read_data("status_data.csv") # importing status dataset
    
    # Changing the dtype of the DateTime column in the imported dataframes.
    fault_df['DateTime']  = pd.to_datetime(fault_df['DateTime'])
    scada_df['DateTime']  = pd.to_datetime(scada_df['DateTime'])
    status_df['Time'] = pd.to_datetime(status_df['Time'])
    
    # Renaming the DateTime columns in all the imported dataset before merge operation
    fault_df.rename(columns={'Time': 'time_fault'}, inplace=True)
    scada_df.rename(columns={'Time': 'time_scada'}, inplace=True)
    status_df.rename(columns={'Time': 'DateTime'}, inplace=True)
    
    
    # Merging the fault dataset and scada dataset
    processed_data = pd.merge(fault_df, scada_df, on="DateTime", how='outer')
    
    # Merging the merged dataset and status dataset
    processed_data = pd.merge(processed_data, status_df, on="DateTime", how='outer')
    
    # saving the processed dataset in the processed folder.
    processed_data.to_csv("../data/processed/processed_dataset.csv", index=False)
    
    return processed_data