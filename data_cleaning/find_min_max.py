import pandas as pd

# Load the CSV data
url = "https://raw.githubusercontent.com/JingXuen/FIT3179_Data-Visualization-2/refs/heads/main/data/pollutants_1922_2022.csv"
data = pd.read_csv(url)

# Filter the data to only include rows where the Entity is 'Malaysia'
malaysia_data = data[data['Entity'] == 'Malaysia']

# Select the pollutant columns
pollutants_columns = [
    'Nitrogen oxide (NOx)',
    'Sulphur dioxide (SO₂) emissions',
    'Carbon monoxide (CO) emissions',
    'Black carbon (BC) emissions',
    'Ammonia (NH₃) emissions',
    'Non-methane volatile organic compounds (NMVOC) emissions'
]

# Find the maximum value for each pollutant column
max_values = malaysia_data[pollutants_columns].max()

# Print the maximum value for each pollutant
for pollutant, max_value in max_values.items():
    print(f"Maximum {pollutant,}: {max_value:.2f}, {malaysia_data[malaysia_data[pollutant] == max_value]['Year'].values[0]}")
