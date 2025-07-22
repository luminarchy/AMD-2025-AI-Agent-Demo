import pandas as pd
from sqlalchemy import create_engine

rep = lambda x: str(x).replace("_x000D_", "").strip()
convert = {}
for i in range(3):
    convert.update({i+1: rep})
pf = pd.read_excel("database.xlsx", header = 0, index_col=0, converters = convert)
pf.index.name = "id"
engine = create_engine('sqlite://', echo=False)
pf.to_sql("hello", engine)
parameter = "name"
parameters = pf.columns.tolist()
if parameter in parameters:
    print(pf)
df ={
    "name": ["p"], "email": ["idk"], "phone": ["2839122109"]
  }
df = pd.DataFrame(df, index = [1])
df.index.name = "id"
print(df)
df.to_sql("hello", engine, if_exists= "append")
with engine.connect() as conn:
   print(pd.read_sql_query("SELECT * FROM hello", conn))
print(pf)

count = 0
def x():
    global count
    count += 2
    return count
x()
print(count)