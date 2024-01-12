import sqlite3
import os
import pandas as pd

con = sqlite3.connect(os.path.abspath('instance\CG.db'))
cur = con.cursor()
query = ''' SELECT fecha, var, sum(vol), sum(value) 
            FROM  cg_db
            GROUP BY  var, fecha
            ORDER BY  var, fecha
            '''
cur.execute(query)
df = pd.DataFrame(cur.fetchall())

print(df)

            