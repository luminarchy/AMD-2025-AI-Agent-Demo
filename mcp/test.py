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
    x = pd.read_sql_query("SELECT * FROM poemsf WHERE Title LIKE \"%" + "The Lake Isle of Innisfree" + "%\" AND Poet LIKE \"%" + "Yeats" + "%\" AND Poet LIKE \"%" + "" + "%\"", conn)
print(x.shape)

title = "The Lake Isle of Innisfree"
author_last = "Yeats"
author_first = ""
with engine.connect() as conn, conn.begin():
    x = pd.read_sql_query(f"SELECT * FROM poemsf WHERE Title LIKE \"%{title} %\" AND Poet LIKE \"%{author_last}%\" AND Poet LIKE \"%{author_first}%\"", conn)
print(x)