# filename: inspect_dataset.py

import requests
import pandas as pd

# Download the CSV file
url = "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv"
response = requests.get(url)
data = response.text

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(pd.compat.StringIO(data))

# Print the first few rows of the dataset
print(df.head())