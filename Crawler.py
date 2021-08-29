import requests
import json
from time import sleep
import pandas as pd
from sqlalchemy import create_engine
from math import ceil

class Crawler():
    def __init__(self):
        self.base_url = 'https://public-apis-api.herokuapp.com/api/v1/'
        self.headers = {}
        self.response = None
        self.category = []
        self.page = 1
        self.apis = []
        self.i = 0
        
        
    def auth(self):
        self.response = requests.get(url = self.base_url+'auth/token')
        self.headers['Authorization']='Bearer '+(json.loads(self.response.text.encode('utf8'))['token'])
        
    def categories(self):
        self.auth()
        while True:
            self.response = requests.get(url = self.base_url+'apis/categories?page='+str(self.page), headers = self.headers)
            self.category.extend(json.loads(self.response.text.encode('utf8'))['categories'])
            max_page = ceil(json.loads(self.response.text.encode('utf8'))['count']/10)
            if self.page == max_page:
                break
            self.page = self.page + 1
        for i in range(len(self.category)):
            if '&' in self.category[i]:
                self.category[i] = self.category[i].replace('&','%26')
        
                
    def get_apis(self):
        self.categories()
        for i in range(self.i,len(self.category)):
            category = self.category[i]
            self.page = 1
            while True:
                error = ''
                try:
                    self.response = requests.get(url = self.base_url+'apis/entry?page='+str(self.page)+'&category='+category, headers = self.headers)
                    error = self.response.content
                    self.apis.extend(json.loads(self.response.text.encode('utf8'))['categories'])
                    max_page = ceil(json.loads(self.response.text.encode('utf8'))['count']/10)
                    if self.page == max_page:
                        self.i = self.i + 1
                        break
                    self.page = self.page + 1
                except Exception:
                    if "error" in error.decode("utf-8"):
                        sleep(38)
                        self.auth()
                    else:
                        sleep(38)
        df = pd.DataFrame(self.apis)
        df.to_csv('results.csv')
        self.db(df)
       
            
    def db(self, df):
        # connect to database
        try:
            engine = create_engine('postgresql://user:pass@db',echo=True)
            df.to_sql('test_table',con = engine,if_exists = 'append',index = False)
            print(pd.DataFrame(engine.execute("select count(*) from test_table").fetchall(),
                  columns=['API','Description','Auth','HTTPS','Cors','Link','Category']).to_string())
        except:
            print('Cannot connect to database')

def main():
    print('API Crawling Started')       
    crawler = Crawler()
    crawler.get_apis()
    print('API Crawling Ended')
    
if __name__ == "__main__":
    main()
