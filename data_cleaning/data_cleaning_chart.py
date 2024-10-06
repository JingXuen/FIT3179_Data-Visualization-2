import pandas as pd

# Load population data and filter for years between 1922 and 2022
df_population = pd.read_csv('https://raw.githubusercontent.com/JingXuen/FIT3179_Week10_Homework/refs/heads/main/data/population.csv')
filtered_df_population = df_population[(df_population['Year'] >= 1922) & (df_population['Year'] <= 2022)]

# Load air pollutants data and filter for years between 1922 and 2022
df_air_pollutants = pd.read_csv('https://raw.githubusercontent.com/JingXuen/FIT3179_Week10_Homework/refs/heads/main/data/amount_of_air_pollutants.csv')
filtered_df_air_pollutants = df_air_pollutants[(df_air_pollutants['Year'] >= 1922) & (df_air_pollutants['Year'] <= 2022)]

df_continent = pd.read_csv('https://raw.githubusercontent.com/JingXuen/FIT3179_Data-Visualization-2/refs/heads/main/data/entity_continent.csv')

# Merge datasets on 'Year', 'Entity', and 'Code'
merged_df = pd.merge(filtered_df_population, filtered_df_air_pollutants, on=['Year', 'Entity', 'Code'], how='inner')

# Add 'Entity_Year' column for joining purposes
merged_df['Entity_Year'] = merged_df['Entity'] + '_' + merged_df['Year'].astype(str)

# Remove all other pollutant columns
columns_to_remove = [
    'Code','Year'
]
df_continent = df_continent.drop(columns=columns_to_remove)

merged_df_continent = pd.merge(merged_df, df_continent, on=['Entity'], how='inner')

# Save the cleaned data to a new CSV file
merged_df_continent.to_csv('pollutants_1922_2022_bubble_chart.csv', index=False)

# Print the first few rows of the resulting dataframe
print(merged_df_continent.head())