import pandas as pd
import numpy as np

def preprocess_price_data(price_data):
    """
    Process price data to generate DateTime and filter for 'HB_HOUSTON' settlement point.

    Parameters:
    ----------
    price_data : pandas.DataFrame
        DataFrame containing the raw price data with 'Delivery Date', 'Hour Ending', and 'Settlement Point'.

    Returns:
    -------
    pandas.DataFrame
        Processed DataFrame with 'DateTime' and filtered rows for 'HB_HOUSTON'.
    """
    price_data['Hour Ending'] = price_data['Hour Ending'].str.replace(':00', ':59', regex=False)
    price_data['DateTime'] = pd.to_datetime(
        price_data['Delivery Date'] + ' ' + price_data['Hour Ending'],
        format='%m/%d/%Y %H:%M',
        errors='coerce'
    )
    return price_data[price_data['Settlement Point'] == 'HB_HOUSTON']

def preprocess_scada_data(scada_data, overlap_start, overlap_end):
    """
    Align SCADA DateTime to nearest hour ending with ':59' and filter within overlapping range.

    Parameters:
    ----------
    scada_data : pandas.DataFrame
        DataFrame containing the raw SCADA data with 'DateTime'.
    overlap_start : pandas.Timestamp
        Start of the overlapping period for filtering.
    overlap_end : pandas.Timestamp
        End of the overlapping period for filtering.

    Returns:
    -------
    pandas.DataFrame
        Filtered and adjusted SCADA DataFrame within the specified range.
    """
    scada_data['DateTime'] = scada_data['DateTime'].dt.floor('H') + pd.Timedelta(minutes=59)
    return scada_data[(scada_data['DateTime'] >= overlap_start) & (scada_data['DateTime'] <= overlap_end)]

def calculate_revenue(scada_data, price_data):
    """
    Merge SCADA and price data, and calculate revenue based on production and price.

    Parameters:
    ----------
    scada_data : pandas.DataFrame
        DataFrame containing 'DateTime' and 'WEC: Production kWh'.
    price_data : pandas.DataFrame
        DataFrame containing 'DateTime' and 'Settlement Point Price'.

    Returns:
    -------
    pandas.DataFrame
        DataFrame containing merged data and calculated revenue.
    float
        Total revenue generated.
    """
    merged_data = scada_data.merge(
        price_data[['DateTime', 'Settlement Point Price']],
        on="DateTime",
        how="inner"
    )
    merged_data['Revenue'] = merged_data['WEC: Production kWh'] * merged_data['Settlement Point Price'] / 1000
    return merged_data, merged_data['Revenue'].sum()

def load_and_preprocess_price_data(price_data_path, sheets):
    """
    Load and preprocess price data for Houston from multiple sheets.

    Parameters:
    ----------
    price_data_path : str
        Path to the Excel file containing price data.
    sheets : list of str
        List of sheet names to load and combine.

    Returns:
    -------
    pandas.DataFrame
        Preprocessed price data for 'HB_HOUSTON'.
    """
    price_data_combined = pd.DataFrame()
    for sheet in sheets:
        sheet_data = pd.read_excel(price_data_path, sheet_name=sheet)
        price_data_combined = pd.concat([price_data_combined, sheet_data], ignore_index=True)
    return preprocess_price_data(price_data_combined)

def load_and_preprocess_scada_data(scada_data_path, overlap_start, overlap_end):
    """
    Load and preprocess SCADA data to align with price data.

    Parameters:
    ----------
    scada_data_path : str
        Path to the CSV file containing SCADA data.
    overlap_start : pandas.Timestamp
        Start of the overlapping period for filtering.
    overlap_end : pandas.Timestamp
        End of the overlapping period for filtering.

    Returns:
    -------
    pandas.DataFrame
        Preprocessed SCADA data within the specified range.
    """
    scada_data = pd.read_csv(scada_data_path)
    scada_data['DateTime'] = pd.to_datetime(scada_data['DateTime'])
    return preprocess_scada_data(scada_data, overlap_start, overlap_end)

def load_and_preprocess_fault_data(fault_data_path):
    """
    Load and preprocess fault data.

    Parameters:
    ----------
    fault_data_path : str
        Path to the CSV file containing fault data.

    Returns:
    -------
    pandas.DataFrame
        Preprocessed fault data with extracted temporal features.
    """
    fault_data = pd.read_csv(fault_data_path)
    fault_data['DateTime'] = pd.to_datetime(fault_data['DateTime'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    fault_data['Day'] = fault_data['DateTime'].dt.date
    fault_data['Month'] = fault_data['DateTime'].dt.month
    return fault_data