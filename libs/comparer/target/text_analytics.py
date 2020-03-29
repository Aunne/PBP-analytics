import requests
from bs4 import   BeautifulSoup

url_origin="https://account.google.com/signin/v2/indentfier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
url_code=requests.get(url=url_origin).text
soup=BeautifulSoup(url_code,'lxml')





"""
https://project.starinc.xyz/pbp_test/test.php
"""