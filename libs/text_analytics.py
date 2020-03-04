import requests
from bs4 import   BeautifulSoup

URL_code=requests.get('https://poyang.netlify.com').text
BS_URL_cd=BeautifulSoup(URL_code,'html.parser')
URL_title=BS_URL_cd.title
