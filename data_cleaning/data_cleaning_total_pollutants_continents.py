import pandas as pd

# Load the data from a CSV file
# Make sure to replace 'path/to/your/data.csv' with the actual path to your data file
data = pd.read_csv('https://raw.githubusercontent.com/JingXuen/FIT3179_Data-Visualization-2/refs/heads/main/data/pollutants_emission_with_continents_1922_2022.csv')

# Calculate the total emissions for each continent and year
# First, create a new column for total pollutants by summing the relevant columns
data['Total_Pollutants'] = (
    data['Nitrogen oxide (NOx)'] +
    data['Sulphur dioxide (SO₂) emissions'] +
    data['Carbon monoxide (CO) emissions'] +
    data['Black carbon (BC) emissions'] +
    data['Ammonia (NH₃) emissions'] +
    data['Non-methane volatile organic compounds (NMVOC) emissions']
)

# Group the data by 'Year' and 'Continent' and sum the total pollutants
total_emissions = data.groupby(['Year', 'Continent'])['Total_Pollutants'].sum().reset_index()

# Define the output file path
output_file = 'total_pollutants_by_continent_year.csv'

# Write the results to a CSV file
total_emissions.to_csv(output_file, index=False)

# Print a confirmation message
print(f"Total emissions have been written to '{output_file}'.")
