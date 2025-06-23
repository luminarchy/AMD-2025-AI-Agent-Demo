import pandas as pd
import pandas.io.sql as sql
from sqlalchemy import create_engine
import numpy as np
import format as f

rep = lambda x: x.replace("_x000D_", "").strip()
pf = pd.read_excel("PoetryFoundationData.xlsx", header = 0, index_col=0, usecols = "A:E", converters = {1: rep, 2: rep, 3: rep, 4: rep})
engine = create_engine('sqlite://', echo=False)
pf.to_sql(name='poemsf', con=engine)

print(pf.shape)
print(pf.columns.values)
authors = ["W.B.Yeats"]
sql = ("SELECT * FROM poemsf WHERE ")
auth = sql + "(Poet LIKE \"%"
auth += "%\" OR Poet LIKE \"%".join(authors)
auth += "%\") "

    

with engine.connect() as conn, conn.begin():
    x = pd.read_sql_query("SELECT * FROM poemsf WHERE Tags LIKE \"%" + "family" + "%\" AND Poet LIKE \"%%\"", conn)
lis = ["hello"]
print("wads".join(lis))

