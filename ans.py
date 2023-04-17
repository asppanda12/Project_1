
import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('articles11.db')

response = requests.get('https://www.theverge.com')
print(response)
url='https://www.theverge.com'
soup = BeautifulSoup(response.text, 'lxml')

links=[]
head=soup.find_all('div',class_="max-w-content-block-standard md:w-content-block-compact md:max-w-content-block-compact lg:w-[240px] lg:max-w-[240px] lg:pr-10")
for h in head:
    ans1=h.find('a').get('href')
    url_links=url+ans1
    links.append(url_links)
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

for l in all_details:
    
    url=l['url']
    headline=l['headline']
    author=l['author']
    date=l['date']
    print(headline)
    conn.execute("INSERT INTO articles (url, headline, author, date) VALUES (?, ?, ?, ?)", (url, headline, author, date))
    conn.commit()
conn.close()
