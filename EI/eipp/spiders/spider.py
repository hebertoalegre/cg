    
import requests 
import scrapy    
import pandas as pd 
import os


from tqdm import tqdm
from eipp.items import EippItem
from datetime import datetime

import locale
locale.setlocale(locale.LC_TIME, 'es_GT')

class cg(scrapy.Spider):
    name = 'cg'
    allowed_domains = ['banguat.gob.gt']
    custom_settings = {'ITEM_PIPELINES': {"eipp.pipelines.EippPipeline": 100}}
    start_urls = ['https://banguat.gob.gt/es/page/comercio-general-version-xlsx',
                  'https://banguat.gob.gt/page/anios-2002-2017-comercio-general'
                  ]

    def parse(self, response):
        lst = []
        for t in response.xpath('//tr/td/p/a/@href'):
            if 'KG-51' in t.get() or 'KF-51' in t.get():
                if t.get().endswith('.xlsx'):
                    relative_url = t.get()
                    absolute_url = response.urljoin(relative_url)
                    resp = requests.get(absolute_url, verify=False, timeout=150)
    
                    if any(int(absolute_url.split('_')[-1].replace('.xlsx', '')) == year for year in [2021,2022,2023]):
                        df = pd.read_excel(resp.content, engine='openpyxl', header=[11,12]).iloc[:,1:]
                    else:
                        df = pd.read_excel(resp.content, engine='openpyxl', header=[7,8])
                    df[df.columns[0]] = df[df.columns[0]].ffill()
                    df[df.columns[1]] = df[df.columns[1]].ffill()
                    df = df.set_index([df.columns[0], df.columns[1], df.columns[2]]).T.unstack().unstack().reset_index()
                    df = df[((df[df.columns[0]]!='TOTALES')|(df[df.columns[0]]!='TOTAL'))]  
                    
                    df.columns = ['PAIS', 'PRODUCTO', 'SAC', 'CARACTERISTICA', 'MES', 'MONTO']
                    df['ANO']=int(absolute_url.split('_')[-1].replace('.xlsx', ''))
                    df = df.drop(df.columns[1], axis=1)
                    df=df.pivot(index=['PAIS', 'SAC', 'ANO', 'MES'], columns='CARACTERISTICA').reset_index()
                    df = df[df[df.columns[3]]!='Total Anual']
                    df = df.dropna(axis=0)
                    df.SAC = [str(int(i)).strip().zfill(8) if len(str(int(i)).strip())==7 else str(int(i)).strip().zfill(10) if len(str(int(i)))==9  else str(int(i)).strip() for i in df.SAC]
                    if 'Origen' in absolute_url:
                        df['var'] = 'Importacion(Origen)'
                    elif 'Vendedor' in absolute_url:
                        df['var'] = 'Importacion(Vendedor)'
                    else:
                        df['var'] = 'Exportacion'

                 
                    df.to_csv(os.path.join(os.path.abspath('outputs'),f'{absolute_url.split("/")[-2]}_{absolute_url.split("/")[-1].replace(".xlsx","")}.csv'), sep=';')            
                    print(df)
                   
          
        #             # item = EippItem()
                    # for row in tqdm(range(df.shape[0])):
                    #     item['pais'] = df.iloc[row,0]
                    #     item['fecha'] = datetime.strptime(str(int(df.iloc[row, 2])) + '-' + df.iloc[row, 3].lower(), '%Y-%B')
                    #     item['sac'] = str(df.iloc[row, 1])
                    #     item['value'] = float(df.iloc[row,4])
                    #     item['vol'] = float(df.iloc[row,5])
                    #     item['var'] = df.iloc[row,6]
                    #     yield item
                        

                 
                      
                      

  


        