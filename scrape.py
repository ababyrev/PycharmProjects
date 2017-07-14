from bs4 import BeautifulSoup
import requests, time, re

URL = "http://all-free-download.com/wallpapers/"

proxies = {'http' : 'proxy.bloomberg.com:81',
           'https': 'proxy.bloomberg.com:81'}

page = requests.get(URL, proxies=proxies)
#print (page.status_code)
#print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# find all img tags that have a class "img-responsive*" and alt tag contains word 'Xbox'
results = soup.find_all("img", class_=re.compile("img-responsive*"), alt=re.compile("Xbox"))

for find in results:
    print (find)
