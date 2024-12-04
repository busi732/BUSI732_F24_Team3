import numpy as np
import pandas as pd

def preprocess_price_data(price_data):
    """
    Process price data to generate DateTime and filter for 'HB_HOUSTON' settlement point.

    - Combines 'Delivery Date' and 'Hour Ending' to create a unified DateTime.
    - Adjusts 'Hour Ending' to end at the 59th minute for consistency.
    - Filters data for the 'HB_HOUSTON' settlement point.

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

    - Adjusts the DateTime to match the granularity of the price data.
    - Filters SCADA data to include only records within the overlapping period.

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

    - Merges SCADA and price data on 'DateTime'.
    - Calculates revenue using the formula: production (kWh) * price ($/MWh) / 1000.

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
    merged_data['Revenue'] = merged_data['WEC: Production kWh'] * merged_data['Settlement Point Price'] / 1000  # Convert kWh to MWh
    return merged_data, merged_data['Revenue'].sum()

def create_temporal_features(df):
    """
    Extracts temporal features from the DateTime column to support seasonal and operational analysis 
    relevant to turbine maintenance and energy production.

    - 'Month': Identifies the month of each record, enabling month-based seasonality analysis.
    - 'Day_of_Week': Extracts the day of the week (0=Monday, 6=Sunday) to analyze trends by day.
    - 'Is_Weekend': Marks weekends (1 if Saturday or Sunday, else 0), allowing comparison of weekend vs. weekday patterns.
    - 'Is_High_Demand_Season': Identifies high-demand season (summer months, June-August, marked as 1), 
       relevant for identifying maintenance needs and operational costs during peak energy demand.

    Parameters:
    ----------
    df : pandas.DataFrame
        DataFrame containing the DateTime column.

    Returns:
    -------
    pandas.DataFrame
        Original DataFrame with new temporal feature columns.
    """
    df['Month'] = df['DateTime'].dt.month
    df['Day_of_Week'] = df['DateTime'].dt.dayofweek
    df['Is_Weekend'] = df['Day_of_Week'].apply(lambda x: 1 if x >= 5 else 0)
    df['Is_High_Demand_Season'] = df['Month'].apply(lambda x: 1 if x in [1, 2, 6, 7, 8] else 0)
    return df

def calculate_fault_frequency(df, fault_column):
    """
    Analyzes frequency of fault occurrences per fault type, supporting predictive maintenance planning.

    - 'Fault Count': Tracks cumulative occurrences of each unique fault type in the dataset.
    - 'Days_Since_Last_Fault': Tracks days since the last recorded occurrence of each fault type,
       which can help predict fault recurrence patterns and intervals.

    Parameters:
    ----------
    df : pandas.DataFrame
        DataFrame containing fault data.
    fault_column : str
        Column name containing fault types or fault occurrence markers.

    Returns:
    -------
    pandas.DataFrame
        DataFrame with fault frequency features added.
    """
    # Count cumulative fault occurrences per day
    df[f'{fault_column}_count'] = df.groupby(fault_column).cumcount() + 1
    
    # Days since last fault
    df['Days_Since_Last_Fault'] = df.groupby(fault_column).cumcount(ascending=False)
    
    return df

def calculate_maintenance_cost(df):
    """
    Calculates estimated maintenance costs per instance based on seasonality and type of service.

    - 'Maintenance_Cost': Cost per maintenance trip, where high demand season costs $150,000 
       (external) and normal season costs $50,000 (external).

    Parameters:
    ----------
    df : pandas.DataFrame
        DataFrame with seasonality information.

    Returns:
    -------
    pandas.DataFrame
        DataFrame with estimated maintenance costs per entry.
    """
    df['Maintenance_Cost'] = np.where(
        (df['Is_High_Demand_Season'] == 1),
        150000,  # High demand season external maintenance cost
        50000  # Normal season external maintenance cost
    )
    # For internal maintenance, add a fixed annual cost per fault type (distributed across entries as an estimate)
    # df['Internal_Maintenance_Cost'] = 750000 / len(df)
    return df

def energy_production_metrics(df, production_column, pre_sold_percentage=0.8):
    """
    Computes metrics related to energy production, based on a pre-sold energy percentage.

    - 'Pre_Sold_Production': Estimated amount of energy pre-sold based on production column and 
       pre_sold_percentage (default 80%).

    Parameters:
    ----------
    df : pandas.DataFrame
        DataFrame containing energy production data.
    production_column : str
        Column name representing actual energy production.
    pre_sold_percentage : float, optional
        Percentage of expected energy production that was pre-sold (default is 0.8 or 80%).

    Returns:
    -------
    pandas.DataFrame
        DataFrame with energy production shortfall and surplus columns.
    """
    df['Pre_Sold_Production'] = df[production_column] * pre_sold_percentage
    return df

