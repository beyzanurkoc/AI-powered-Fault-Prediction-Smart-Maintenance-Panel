import pandas as pd
import numpy as np

df = pd.read_csv("data_clean.csv")  

new_rows = []

# For each code, create 5 random samples !!!
for idx, row in df.iterrows():
    for i in range(5):
        new_row = {
            "code": row["code"],
            "description": row["description"],
            "temperature": np.random.randint(60, 150),
            "pressure": round(np.random.uniform(0.8, 3.5), 2),
            "engine_rpm": np.random.randint(800, 2000)
        }
        new_rows.append(new_row)

df_expanded = pd.DataFrame(new_rows)
df_expanded.to_csv("sample_data.csv", index=False)

print("sample_data.csv created with 5 samples for each fault code!")
print(df_expanded.head(10))
