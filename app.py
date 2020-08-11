import sys
import requests
import pandas
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable flag warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


company_code = sys.argv[1]
def crawling(numpage):
    data = []

    for i in range(numpage + 1):
        page = i + 1
        url = "https://finance.naver.com/item/board.nhn?code="+ company_code + "&page=%s"%page
        ua = UserAgent(use_cache_server=False,verify_ssl=False)
        headers={'User-Agent': ua.random}
        r = requests.get(url, headers = headers, verify = False)
        soup = BeautifulSoup(r.text, 'html.parser')
        a = soup.find_all('td', {'class': 'title'})
        for i in a:
            data.append({"title": i.find('a')['title'], "link": i.find('a')['href']})
            
    return(data)

crawled_data = crawling(1)


f=open('test.txt', 'w')
f.write(str(crawled_data))
f.close()
print("done")