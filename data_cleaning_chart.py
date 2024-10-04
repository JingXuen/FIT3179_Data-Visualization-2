import pandas as pd

# Load population data and filter for years between 1922 and 2022
df_population = pd.read_csv('https://raw.githubusercontent.com/JingXuen/FIT3179_Week10_Homework/refs/heads/main/data/population.csv')
filtered_df_population = df_population[(df_population['Year'] >= 1922) & (df_population['Year'] <= 2022)]

# Load air pollutants data and filter for years between 1922 and 2022
df_air_pollutants = pd.read_csv('https://raw.githubusercontent.com/JingXuen/FIT3179_Week10_Homework/refs/heads/main/data/amount_of_air_pollutants.csv')
filtered_df_air_pollutants = df_air_pollutants[(df_air_pollutants['Year'] >= 1922) & (df_air_pollutants['Year'] <= 2022)]

# Merge datasets on 'Year', 'Entity', and 'Code'
merged_df = pd.merge(filtered_df_population, filtered_df_air_pollutants, on=['Year', 'Entity', 'Code'], how='inner')

# Save the cleaned data to a new CSV file
merged_df.to_csv('pollutants_1922_2022.csv', index=False)

# Print the first few rows of the resulting dataframe
print(merged_df.head())