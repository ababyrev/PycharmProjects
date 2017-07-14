from bs4 import BeautifulSoup
import requests, time, re

URL = "https://www.pexels.com/search/nature%20wallpaper/"

proxies = {'http' : 'proxy.bloomberg.com:81',
           'https': 'proxy.bloomberg.com:81'}

page = requests.get(URL, proxies=proxies)
#print (page.status_code)
#print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("a", title=re.compile("Green"))

for find in results:
    print (find)
