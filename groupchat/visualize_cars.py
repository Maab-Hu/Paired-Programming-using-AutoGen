# filename: visualize_cars.py

import requests
import pandas as pd
import io
import matplotlib.pyplot as plt

# Download the CSV file
url = "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv"
response = requests.get(url)
data = response.text

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(io.StringIO(data))

# Print the fields in the dataset
print(df.columns)

# Plot the relationship between weight and horsepower
plt.scatter(df['weight'], df['horsepower'])
plt.xlabel('Weight')
plt.ylabel('Horsepower')
plt.title('Relationship between Weight and Horsepower')
plt.savefig('car_visualization.png')
plt.show()