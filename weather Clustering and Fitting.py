import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
import io

# Upload the CSV file
uploaded = files.upload()
filename = next(iter(uploaded))

# Load the dataset
df = pd.read_csv(io.BytesIO(uploaded[filename]))

# Replace 'NA' with NaN and convert columns to proper data types
df.replace('NA', np.nan, inplace=True)
df['Rainfall'] = pd.to_numeric(df['Rainfall'], errors='coerce')
df['MaxTemp'] = pd.to_numeric(df['MaxTemp'], errors='coerce')
df['WindGustSpeed'] = pd.to_numeric(df['WindGustSpeed'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])

# Impute missing values for numerical columns with the median
for col in ['Rainfall', 'MaxTemp', 'WindGustSpeed']:
    df[col].fillna(df[col].median(), inplace=True)

# Set the Date as the index
df.set_index('Date', inplace=True)

# Time series plot of Rainfall
plt.figure(figsize=(14, 6))
df['Rainfall'].plot(title='Rainfall over Time')
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.show()

# Histogram of Max Temperature
plt.figure(figsize=(10, 6))
sns.histplot(df['MaxTemp'], kde=True)
plt.title('Distribution of Maximum Temperature')
plt.xlabel('Maximum Temperature (°C)')
plt.ylabel('Frequency')
plt.show()

# Boxplot for Wind Gust Speed to check for outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['WindGustSpeed'])
plt.title('Boxplot of Wind Gust Speed')
plt.xlabel('Wind Gust Speed (km/h)')
plt.show()