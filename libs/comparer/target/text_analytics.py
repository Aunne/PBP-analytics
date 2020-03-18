import requests
from bs4 import   BeautifulSoup

Server_specimen_URL="AAA"  #AAA為資料庫"資料網址"
Client_test_ULR="BBB"  #BBB為用戶端測試"比對網址"

Client_test_code=requests.get("url=Cliien_test_URL").text

for URL in Server_specimen_URL







"""
URL_code=requests.get('https://project.starinc.xyz/pbp_test/test.php').text
BS_URL_cd=BeautifulSoup(URL_code,'html.parser')
URL_Tag_text=BS_URL_cd.get_text()
A=URL_Tag_text.replace("\n","").replace("\r","")
print(A.text)
""'
