import pandas as pd

# Change the file path to your CSV file's actual location if needed
file_path = "data_clean.csv"  #fault code & description 

# Read the CSV file
df = pd.read_csv(file_path)

# Show all rows 
print(df)

