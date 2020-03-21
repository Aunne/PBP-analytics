import requests
from bs4 import   BeautifulSoup

class Exract :
    def __init__(self) :
        self.URL=""
        self.URL_code=requests().get("url=URL").text
        Bt4S_URL_parser_code=BeautifulSoup(self.URL_code,"html.parser")
    def Html_tag_parser (self) :
         Code_tag_tandem=[]
         Code_tag=find_all(['p','pre','h1','h2','h3','h4','h5','h6','b','i','u','sup','sub','font','li','a','caption',
         'th','td',''])



    def Slice_tag (self) :

Client=Exract()
Server_specimen_URL="AAA" #AAA為資料庫"資料網址"
Client.URL="BBB"  #BBB為用戶端測試"比對網址"










"""
URL_code=requests.get('https://project.starinc.xyz/pbp_test/test.php').text
BS_URL_cd=BeautifulSoup(URL_code,'html.parser')
URL_Tag_text=BS_URL_cd.get_text()
A=URL_Tag_text.replace("\n","").replace("\r","")
print(A.text)
""'
