from bs4 import BeautifulSoup
import requests, time, re

URL = "http://all-free-download.com/wallpapers/"

proxies = {'http' : 'proxy.bloomberg.com:81',
           'https': 'proxy.bloomberg.com:81'}

page = requests.get(URL, proxies=proxies)
#print (page.status_code)
#print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# find all img tags that have a class "img-responsive*"
results = soup.find_all("img", class_=re.compile("img-responsive*"))

for find in results:
    print (find)
