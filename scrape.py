from bs4 import BeautifulSoup
import requests
import time

proxies = {'http' : 'proxy.bloomberg.com:81',
           'https': 'proxy.bloomberg.com:81'}

page = requests.get("https://www.dataquest.io/blog/web-scraping-tutorial-python/",proxies=proxies)
#print (page.status_code)
#print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

list_len = len(soup.find_all('p'))

print (list_len)
element = 0
while element <= list_len:
    print (soup.find_all('p')[element].get_text())
    element += 1
    time.sleep (2)
    print (element)