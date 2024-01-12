import pandas as pd 
import sqlite3  
import os
from tqdm import tqdm
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_GT')


route = os.path.abspath('outputs')
files = os.listdir(route)
#Conect
con = sqlite3.connect(os.path.abspath('instance\CG.db'))

#####################################################################################
#                                                                                   #
#                               DELETE DATA FROM SQLITE                             #
#                                                                                   #
#####################################################################################
sql = 'DELETE FROM cg_db'

cur = con.cursor()
cur.execute(sql)
con.commit()


#####################################################################################
#                                                                                   #
#                                   ADDING NEW DATA                                 #
#                                                                                   #
#####################################################################################

for file in tqdm(files):
    df = pd.read_csv(os.path.join(route, file), sep=';', header=0).iloc[1:,1:]
    df.columns  =['pais', 'sac','ano','mes','value', 'vol','var']
    df.sac = [str(int(i)).strip().zfill(8) if len(str(int(i)).strip())==7 else str(int(i)).strip().zfill(10) if len(str(int(i)))==9  else str(int(i)).strip() for i in df.sac]
    df.loc[:,'fecha'] = (df.loc[:, 'ano'].astype(int).astype(str) + '-' + df.loc[:, 'mes'].apply(lambda x: str(x).lower())).apply(lambda x: datetime.strptime(x, '%Y-%B'))
    df = df[['pais', 'fecha', 'sac','value','vol','var']]   
    df.to_sql('cg_db', con=con, chunksize=1000, if_exists='append', index=False)

print('exito')

con.close()
