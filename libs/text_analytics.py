import requests
from bs4 import   BeautifulSoup

class Biopsy :                  #原始碼切片物件
    def  __init__(self) :    ＃初始值
    def  Client_URL_analyze(Client_giving_URL=None) :  #客戶端網址解析器
    def  Client_URL_code_analyze() :    #客戶端原始碼解析器
        



URL_code=requests.get('https://project.starinc.xyz/pbp_test/test.php').text
BS_URL_cd=BeautifulSoup(URL_code,'html.parser')
URL_Tag_text=BS_URL_cd.get_text()
A=URL_Tag_text.replace("\n","").replace("\r","")
print(A.text)

