import pandas as pd

def extract_json(json_path):
 return pd.read_json(json_path)

def extract_csv(csv_path):
 return pd.read_csv(csv_path)

def extract_excel(excel_path):
 return pd.read_excel(excel_path)

# Additional extraction functions for XML and HTML can be added as needed
