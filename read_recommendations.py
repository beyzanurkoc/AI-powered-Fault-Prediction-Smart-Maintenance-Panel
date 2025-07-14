import pandas as pd

recommendations = pd.read_csv("recommendations.csv")

suggestion_map = dict(zip(recommendations["code"], recommendations["recommendation"]))



