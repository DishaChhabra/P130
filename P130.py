import pandas as pd

data = pd.read_csv("Projects/P130/finaldata.csv")

del data["Star_name"]
data = data.dropna()
data.to_csv('Projects/P130/data.csv')