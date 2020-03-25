import requests
from bs4 import   BeautifulSoup

url_origin="https://www.google.com"
url_code=requests.get(url=url_origin).text
soup=BeautifulSoup(url_code,'html.parser')

print(soup.b)



"""
URL_code=requests.get('https://project.starinc.xyz/pbp_test/test.php').text
BS_URL_cd=BeautifulSoup(URL_code,'html.parser')
URL_Tag_text=BS_URL_cd.get_text()
A=URL_Tag_text.replace("\n","").replace("\r","")
print(A.text)
"""