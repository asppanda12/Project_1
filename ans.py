import requests
from bs4 import BeautifulSoup
import sqlite3
import os
class Verge:
    def __init__(self):
        self.conn = sqlite3.connect("mydatabase.db")
        self.conn.execute('''CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT,url TEXT,headline TEXT,author TEXT,date TEXT)''')    
        self.response = requests.get('https://www.theverge.com')    
        self.url='https://www.theverge.com'
    def fetch_all_details_using_links(self,links):
        all_details=[]
        for link in links:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'lxml')
            head=soup.find_all('div',class_="flex-col lg:flex lg:ml-40")
            tup=()
            for h in head:
                ans = h.find('h1').text
        
                ans1=h.find('a').text
        
                time=h.find('time').text
        
                map={}
    
                map['url']=link
                map['headline']=ans
                map['author']=ans1
                map['date']=time
                # tup=(link)
                all_details.append(map)
        return all_details   
    def put_all_details_database(self,all_details):
        for l in all_details:
            url=l['url']
            headline=l['headline']
            author=l['author']
            date=l['date']
            self.conn.execute("INSERT INTO articles (url, headline, author, date) VALUES (?, ?, ?, ?)", (url, headline, author, date))
            self.conn.commit()
        self.conn.close()
        return "YOUR DATA ADDED SUCCESSFULLY"
    def start_acumalating_data(self):
        soup = BeautifulSoup(self.response.text, 'lxml')
        links=[]
        head=soup.find_all('div',class_="max-w-content-block-standard md:w-content-block-compact md:max-w-content-block-compact lg:w-[240px] lg:max-w-[240px] lg:pr-10")
        for h in head:
            ans1=h.find('a').get('href')
            url_links=self.url+ans1
            links.append(url_links)
        all_details=[]
        all_details=self.fetch_all_details_using_links(links)
        print(self.put_all_details_database(all_details))
if __name__=="__main__":
    obj=Verge()
    obj.start_acumalating_data()


        