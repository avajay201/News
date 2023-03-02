from django.test import TestCase
from newsapi import NewsApiClient
import mysql.connector
 
 
print('Connecting to DB...')
conn = mysql.connector.connect(user = 'root',
                               host = 'localhost',
                              database = 'database_name')
 
print(conn)
 
# Disconnecting from the server
conn.close()

newsapi = NewsApiClient(api_key = '3586362b1b4d46cdb10f5bed310ca3b7')
# top_headlines = newsapi.get_top_headlines(q ='bitcoin', sources = 'bbc-news,the-verge', category = 'business', language = 'en', country = 'us')
all_articles = newsapi.get_everything(q='tesla',
                                from_param='2023-02-02',
                                language='en',
                                sort_by='relevancy',)

# sources = newsapi.get_sources()
print('>>>>>>>>>status>>>>>>>>>>', all_articles['status'])
if all_articles['status'] == 'ok':
    print('>>>>>>>>>>totalResults>>>>>>>>>', all_articles['totalResults'])
    print('>>>>>>>>>articles len>>>>>>>>>>', len(all_articles['articles']))
    for article in all_articles['articles']:
        print('Author >>>>>>>>', article['author'])
        print('Title >>>>>>>>', article['title'])
        print('Description >>>>>>>>', article['description'])
        print('URL >>>>>>>>', article['url'])
        print('URL Image >>>>>>>>', article['urlToImage'])
        print('Pub Date >>>>>>>>', article['publishedAt'])
        print('Content >>>>>>>>', article['content'])
        break