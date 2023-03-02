from django.test import TestCase
from newsapi import NewsApiClient
import mysql.connector
from datetime import datetime

def news_data():
    try:
        newsapi = NewsApiClient(api_key = '3586362b1b4d46cdb10f5bed310ca3b7')
        all_articles = newsapi.get_everything(q = 'tesla', from_param = '2023-02-03', language = 'en', sort_by = 'relevancy')
        if all_articles['status'] == 'ok':
            print('Total results -', all_articles['totalResults'], '\n')
            print('Total articles -', len(all_articles['articles']), '\n')
            response = {
                'status': True,
                'data': all_articles['articles']
            }
            return response
        else:
            response = {
                'status': False
            }
            return response
    except Exception as err:
        response = {
            'status': 'Error',
            'error': err.__dict__['exception']['message']
        }
        return response

try:
    print('Connecting to DB...\n')
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="news", auth_plugin = 'mysql_native_password')
    print('Successfully connected to DB.\n')
    print('Getting news data...\n')
    data_result = news_data()
    if data_result['status'] == True:
        for data in data_result['data']:
            title = data['title']
            summary = data['description']
            author = data['author']
            image_url = data['urlToImage']
            content = data['content']
            pub_date = data['publishedAt']
            tem_pub_date = '2000-02-01 02:02:02'
            if pub_date:
                pub_date = pub_date.replace('T', ' ').replace('Z', ' ')
                pub_date = datetime.strptime(pub_date, '%Y-%m-%d %H:%M:%S')
            else:
                pub_date = datetime.strptime(tem_pub_date, '%Y-%m-%d %H:%M:%S')
            print('pub_date >>>>>>>', pub_date, '\n')
            break
        print('News data get successfully.\n')
    elif data_result['status'] == 'Error':
        print('News data getting failed -', data_result['error'], '\n')
    else:
        print('Request failed.\n')
except Exception as err:
    print('Script failed -', err)

# 
# # top_headlines = newsapi.get_top_headlines(q ='bitcoin', sources = 'bbc-news,the-verge', category = 'business', language = 'en', country = 'us')

# # sources = newsapi.get_sources()
# print('>>>>>>>>>status>>>>>>>>>>', all_articles['status'])
# if all_articles['status'] == 'ok':
#     print('>>>>>>>>>>totalResults>>>>>>>>>', all_articles['totalResults'])
#     print('>>>>>>>>>articles len>>>>>>>>>>', len(all_articles['articles']))
#     for article in all_articles['articles']:
#         print('Author >>>>>>>>', article['author'])
#         print('Title >>>>>>>>', article['title'])
#         print('Description >>>>>>>>', article['description'])
#         print('URL >>>>>>>>', article['url'])
#         print('URL Image >>>>>>>>', article['urlToImage'])
#         print('Pub Date >>>>>>>>', article['publishedAt'])
#         print('Content >>>>>>>>', article['content'])
#         break