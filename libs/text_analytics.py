import requests
from bs4 import   BeautifulSoup

class Biopsy ():                  #原始碼切片物件
    def  __init__(self) :    #初始值
        self.Server_giving_URL=None    
        self.Client_giving_URL=None
    def  URL_analyze()  :  #網址解析器  網址拆解
        Server_URL_Tandem=self.Server_giving_URL
        Client_URL_Tandem=self.Client_giving_URL



    def  URL_code_analyze() :    #原始碼解析器   原始碼拆解
        

Biopsy().Server_giving_URL=AAA  #AAA為伺服器資料庫網址端口
Biopsy().Client_giving_URL=BBB  #BBB為客戶端傳來的網址端口










"""
URL_code=requests.get('https://project.starinc.xyz/pbp_test/test.php').text
BS_URL_cd=BeautifulSoup(URL_code,'html.parser')
URL_Tag_text=BS_URL_cd.get_text()
A=URL_Tag_text.replace("\n","").replace("\r","")
print(A.text)
""'
