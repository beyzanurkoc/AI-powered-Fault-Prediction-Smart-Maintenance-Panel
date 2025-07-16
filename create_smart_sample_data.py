import pandas as pd
import numpy as np

codes = [
    ("E006", 70, 85, 1.5, 2.0, 1100, 1300), 
    ("S011", 80, 105, 0.8, 1.2, 900, 1150), 
    ("AMB03", 95, 120, 2.1, 2.8, 600, 900), 
    ("FP100", 95, 120, 0.8, 1.2, 1300, 1600),
    ("FS01",  120, 150, 2.5, 3.5, 1000, 1400),
    ("VMS17",  80, 110, 1.2, 2.0, 1000, 1350),
    ("ENG_OIL_PRES_LOW", 95, 115, 0.9, 1.4, 1100, 1400),
    ("ENG_COOL_TEMP_HIGH", 120, 150, 1.4, 2.0, 1000, 1350),
    ("TR_OIL_TEMP_HIGH",  110, 130, 1.2, 1.8, 1100, 1400),
    ("TR_HYD_PRES_LOW",  90, 110, 0.8, 1.2, 950, 1200),
    ("ELEC_BAT_LOW", 60, 80, 1.0, 1.5, 850, 1150),
    ("ELEC_ALT_ERR", 80, 100, 1.3, 1.9, 1200, 1350),
    ("COOL_LVL_LOW", 100, 125, 1.0, 1.7, 1000, 1300),
    ("COOL_FAN_ERR", 105, 130, 1.5, 2.2, 900, 1200),
    ("AMPH_PROP_ERR", 90, 115, 2.0, 2.8, 700, 950),
    ("AMPH_PUMP_PRES_LOW", 95, 120, 0.8, 1.2, 1100, 1500),
    ("AMPH_SEAL_ERR", 80, 110, 1.0, 1.7, 900, 1250),
    ("FIRE_DET_ACT", 130, 160, 2.0, 3.2, 1000, 1400),
    ("FIRE_SYS_ERR", 90, 120, 1.8, 2.8, 950, 1250),
    ("OBS_CAM_ERR", 65, 90, 1.0, 1.6, 800, 1050),
    ("OBS_SENS_ERR", 70, 95, 1.1, 1.7, 900, 1200),
    ("WPN_SYS_ERR", 90, 120, 1.3, 2.0, 1200, 1450)
]

rows = []

for code,t_min, t_max, p_min, p_max, rpm_min, rpm_max in codes:
    for i in range(50): 
        row = {
            "code": code,
            "temperature": np.random.randint(t_min, t_max + 1),
            "pressure": round(np.random.uniform(p_min, p_max), 2),
            "engine_rpm": np.random.randint(rpm_min, rpm_max + 1)
        }
        rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("sample_data.csv", index=False)

print("sample_data.csv created with extended realistic sensor ranges")
print(df.to_string())
