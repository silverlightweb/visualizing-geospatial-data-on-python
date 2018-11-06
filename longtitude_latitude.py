#Extracting  longtitude and latitude
# print the first few rows of df 
import pandas as pd 

df = pd.read_csv("./data/building_permits_2017.csv")
print(df.head())

# extract latitude to a new column: lat
df['lat'] = [loc[0] for loc in df.Location]

# extract longitude to a new column: lng
df['lng'] = [loc[1] for loc in df.Location]

# print the first few rows of df again
print(df.head())
