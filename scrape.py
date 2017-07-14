from bs4 import BeautifulSoup
import requests, time, re

URL = "https://scrapethissite.com/pages/forms/"

proxies = {'http' : 'proxy.bloomberg.com:81',
           'https': 'proxy.bloomberg.com:81'}

page = requests.get(URL, proxies=proxies)
#print (page.status_code)
#print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# pagination
link_tags = soup.select('.pagination a')

for link_tag in link_tags:
    url = link_tag.get('href')
    print (url)

    # find all img tags that have a class "img-responsive*" and alt tag contains word 'Xbox'
    results = soup.find_all("img", class_=re.compile("img-responsive*"), alt=re.compile("Xbox"))

    for find in results:
        print (find)
