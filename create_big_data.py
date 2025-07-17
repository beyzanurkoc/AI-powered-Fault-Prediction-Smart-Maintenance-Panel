import pandas as pd
import random

ROW_COUNT = 50000 

data = []
for _ in range(ROW_COUNT):
    temperature = random.randint(60, 150)
    pressure = round(random.uniform(1.0, 3.5), 2)
    engine_rpm = random.randint(900, 1500)
    data.append({
        "temperature": temperature,
        "pressure": pressure,
        "engine_rpm": engine_rpm
    })

df = pd.DataFrame(data)
df.to_csv("bigdata.csv", index=False)
print(f"bigdata.csv created with {ROW_COUNT} rows!")
