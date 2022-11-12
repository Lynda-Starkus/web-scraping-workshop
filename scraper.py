#This library lets us manipulate the HTML response
from bs4 import BeautifulSoup
#Requests enable us to retrieve HTML/XML files from urls
import requests
#Pandas is used to manipulate tables
import pandas as pd

#Always add this header otherwise the targeted URL will suspect that it's not a human-made request but a bot :3 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

url_inspiration = "https://startupnation.com/category/start-your-business/get-inspired/"
url_growth_hacks = "https://startupnation.com/tag/growth-hacks/"
url_business_life = "https://startupnation.com/tag/business-and-life-planning/"


data_inspiration = requests.get(url_inspiration, headers=headers)
data_growth_hacks = requests.get(url_growth_hacks, headers=headers)
data_business_life = requests.get(url_business_life, headers=headers)


soup_inspiration = BeautifulSoup(data_inspiration.text, 'html.parser')
soup_growth_hacks = BeautifulSoup(data_growth_hacks.text, 'html.parser')
soup_business_life = BeautifulSoup(data_business_life.text, 'html.parser')



df = pd.DataFrame(columns=['title', 'url', 'tag'])
#print(soup_inspiration.prettify())
#print(len(soup_inspiration.find_all('article')))
articles_inspiration = soup_inspiration.find_all('article')
articles_growth_hacks = soup_growth_hacks.find_all('article')
articles_business_life = soup_business_life.find_all('article') 

urls = []
titles = []
tags = []

for article in articles_inspiration:
    content = article.find('h2')
    title = content.text
    href = content.find('a', href=True).attrs["href"]
    
    urls.append(href)
    titles.append(title)
    tags.append('inspiration')

for article in articles_growth_hacks:
    content = article.find('h2')
    title = content.text
    href = content.find('a', href=True).attrs["href"]
    
    urls.append(href)
    titles.append(title)
    tags.append('growth-hacks')

for article in articles_business_life:
    content = article.find('h2')
    title = content.text
    href = content.find('a', href=True).attrs["href"]
    
    urls.append(href)
    titles.append(title)
    tags.append('business-life')


df['title'] = titles
df['url'] = urls
df['tag'] = tags
    
df.to_csv("startupnation_articles.csv")

'''
with open('ctp_output.txt', 'w') as f:
    for tag in soup_inspiration.find_all('p'):
        f.write(tag.text.encode('utf-8') + '\n')
'''