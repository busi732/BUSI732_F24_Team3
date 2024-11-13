from src.data_ingestion import process_raw_data
from dataprep.eda import create_report
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Load the data
processed_df = process_raw_data()

# Generate an EDA report
eda_report = create_report(processed_df)

# Saving it to the 
eda_report.save("../reports/eda_report.html")
