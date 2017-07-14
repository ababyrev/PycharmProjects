from bs4 import BeautifulSoup
import requests, time, re
from urllib.parse import urlparse


URL = "https://scrapethissite.com/pages/forms/"
parsed_url = urlparse(URL)
domain = parsed_url.netloc
protocol = parsed_url.scheme

proxies = {'http' : 'proxy.bloomberg.com:81',
           'https': 'proxy.bloomberg.com:81'}

page = requests.get(URL, proxies=proxies)
#print (page.status_code)
#print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# pagination - find a href with pagination class
link_tags = soup.select('.pagination a')

for link_tag in link_tags:
    url = link_tag.get('href')

    # get URl of next page and instantiate a new soup object
    next_page = requests.get(protocol+"://"+domain+url, proxies=proxies)
    soup = BeautifulSoup(next_page.content, 'html.parser')

    print (next_page.content)

    # find all img tags that have a class "img-responsive*" and alt tag contains word 'Xbox'
    results = soup.find_all("td", class_=re.compile("wins"))

    for find in results:
        print (find)
