import requests
from bs4 import BeautifulSoup
import mysql.connector
import json 

cnx=mysql.connector.connect(user="root",password='',host='127.0.0.1',database='scrapingdatabase')
cursor=cnx.cursor()
try:
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(r.content, features='xml')
         # select only the "items" I want from the data
        articles = soup.findAll('item')

        # for each "item" I want, parse it into a list
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
             
            cursor.execute('INSERT INTO article VALUES(%s,%s,%s)',( title , link , published))
        
except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
cnx.commit()
cnx.close() 
print("finished database filling")
