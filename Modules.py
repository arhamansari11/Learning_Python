import pandas as pd

df = pd.read_json("modules.json", encoding="utf-8")
print(df)
