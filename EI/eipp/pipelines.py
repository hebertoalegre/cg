# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3 
import os

class EippPipeline:
    def __init__(self):
        self.route = os.path.join(os.path.abspath('instance'), 'CG.db')
        self.con = sqlite3.connect(self.route)
        self.cur = self.con.cursor()
        self.cur.execute('''
                         CREATE TABLE IF NOT EXISTS cg_db(
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             pais TEXT,
                             fecha DATE,
                             sac TEXT,
                             value FLOAT,
                             vol FLOAT,
                             var TEXT)                         
                         ''')
    def process_item(self, item, spider):
        self.cur.execute('''
                         SELECT * FROM cg_db WHERE pais = ? 
                         AND fecha =? AND sac = ? AND
                         var = ?                         
                         ''', (item['pais'], item['fecha'], item['sac'], item['var']))
        result = self.cur.fetchone()
        if result:
            self.cur.execute('''
                             UPDATE cg_db SET value =?, vol = ?
                             WHERE id =?''', 
                             (item['value'], item['vol'], result[0])) 
        else:
            self.cur.execute("""
                INSERT INTO cg_db (pais, fecha, sac, value, vol, var) VALUES (?,?,?,?,?,?)
            """,
            (   item['pais'],
                item['fecha'],
                item['sac'],
                item['value'],
                item['vol'],
                item['var']))
        
        self.con.commit()
        return item
