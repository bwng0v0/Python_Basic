from bs4 import BeautifulSoup as bs
import requests

url = "https://www.python.org/"
html = requests.get(url)

soup = bs(html.text,'html.parser')
main_container = soup.find('section', attrs={"class":"main-content"})
target_data = main_container.find(text="Latest News").parent.findNext('ul')

latest_news_dict = {}
for li in target_data.findAll('li'):
    latest_news_dict[li.time.text] = li.a.text

for k,v in latest_news_dict.items():
    print(k,v)