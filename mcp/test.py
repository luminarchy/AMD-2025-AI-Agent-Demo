# import pandas as pd
# import pandas.io.sql as sql
# from sqlalchemy import create_engine
# import numpy as np
# from poemtools import pf

# engine = create_engine('sqlite://', echo=False)
# pf.to_sql(name='poemsf', con=engine)

# print(pf.shape)
# print(pf.columns.values)

# with engine.connect() as conn, conn.begin():
#     x = pd.read_sql_query("SELECT Title FROM poemsf WHERE Poet LIKE \"%" + "yeats" + "%\"", conn)
# print(x)
authors = ["hello", "hello"]
print(f"SELECT * FROM VALUE (\"%{"%\", \"%".join(authors)}%\") AS TableAlias(Col1)")


