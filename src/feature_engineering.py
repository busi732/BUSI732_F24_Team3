import numpy as np

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
    df['Is_High_Demand_Season'] = df['Month'].apply(lambda x: 1 if x in [1, 10, 11, 12] else 0)
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

