import pandas as pd
import pandas.io.sql as sql
from sqlalchemy import create_engine
import numpy as np

rep = lambda x: x.replace("_x000D_", "").strip()
pf = pd.read_excel("PoetryFoundationData.xlsx", header = 0, index_col=0, usecols = "A:E", converters = {1: rep, 2: rep, 3: rep, 4: rep})
engine = create_engine('sqlite://', echo=False)
pf.to_sql(name='poemsf', con=engine)

print(pf.shape)
print(pf.columns.values)
def format_entry(entry: pd.DataFrame):
    poem = {"Title": entry["Title"][0], "Poem": entry["Poem"][0], "Poet": entry["Poet"][0], "Tags": entry["Tags"][0]}
    return poem

with engine.connect() as conn, conn.begin():
    x = pd.read_sql_query("SELECT DISTINCT * FROM poemsf WHERE Title LIKE \"%" + "the second coming" + "%\" AND Poet LIKE \"%yeats%\"", conn)
print(format_entry(x))


