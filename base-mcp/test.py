import pandas as pd
from sqlalchemy import create_engine

rep = lambda x: str(x).replace("_x000D_", "").strip()
convert = {}
for i in range(3):
    convert.update({i+1: rep})
pf = pd.read_excel("database.xlsx", header = 0, index_col=0, converters = convert)
engine = create_engine('sqlite://', echo=False)
print(pf)