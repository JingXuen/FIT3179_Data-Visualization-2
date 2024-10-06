import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/JingXuen/FIT3179_Data-Visualization-2/refs/heads/main/data/pollutants_1922_2022.csv')

# Group by 'Continent' and 'Year', then sum all pollutants
aggregated_df = df.groupby(['Continent', 'Year']).agg({
    'Nitrogen oxide (NOx)': 'sum',
    'Sulphur dioxide (SO₂) emissions': 'sum',
    'Carbon monoxide (CO) emissions': 'sum',
    'Black carbon (BC) emissions': 'sum',
    'Ammonia (NH₃) emissions': 'sum',
    'Non-methane volatile organic compounds (NMVOC) emissions': 'sum'
}).reset_index()

# Display the aggregated result
print(aggregated_df)

# Save the aggregated result to a new CSV file (if needed)
aggregated_df.to_csv('aggregated_pollutants_by_continent_year.csv', index=False)
