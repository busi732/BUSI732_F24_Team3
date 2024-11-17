import pandas as pd

def data_ingestion(file_path, sheet_names=None):
    """
    Load data from a single or multiple sheets in an Excel file.

    - This function reads Excel sheets and combines them into a single DataFrame.
    - If sheet names are not provided, all sheets in the file will be loaded.
    - Designed for loading price data with multiple monthly sheets.

    Parameters:
    ----------
    file_path : str
        The path to the Excel file containing the data.
    sheet_names : list of str, optional
        List of sheet names to load. If None, all sheets in the Excel file are loaded.

    Returns:
    -------
    pandas.DataFrame
        A DataFrame containing all combined data from the specified sheets.
    """
    DATA_PATH = "../data/raw/"
    file_path = DATA_PATH+file_path

    if sheet_names is None:  # If no sheet names are provided, load all sheets
        sheet_names = pd.ExcelFile(file_path).sheet_names

    data_combined = pd.DataFrame()

    for sheet in sheet_names:
        try:
            monthly_data = pd.read_excel(file_path, sheet_name=sheet)
            data_combined = pd.concat([data_combined, monthly_data], ignore_index=True)
        except Exception as e:
            print(f"Error loading sheet {sheet}: {e}")

    return data_combined

