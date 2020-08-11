import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable flag warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ua = UserAgent(use_cache_server=False,verify_ssl=False)
headers={'User-Agent': ua.random}

company_code = "005930"
list =  pd.DataFrame()
def crawling(numpage):
    page = 5
    url = "https://finance.naver.com/item/board.nhn?code="+ company_code + "&page=%s"%page
    print(url)
    df = pd.read_html(requests.get(url, headers = headers, verify = False).text)
    df = df[1].dropna(axis=0, thresh=5)
    print(df)
    list.append(df)

crawled_data = crawling(1)

print(list)
# f=open('test.txt', 'w')
# f.write(str(crawled_data))  
# f.close()
# print("done")