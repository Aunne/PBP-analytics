import requests
from bs4 import   BeautifulSoup

url_origin="https://project.starinc.xyz/pbp_test/test.php"
url_code=requests.get(url=url_origin).text
soup=BeautifulSoup(url_code,'lxml')

if '登入' in soup.title.string :
    print("yes")
else :
    for tag_input in soup('input') :
        if '登入' in str(tag_input) :
            print('yes')

    


"""
def remove_tags(code_handle) :
    return ''.join(xml.etree.ElementTree.fromstrig(soup_handle).itertext())

soup_handle=soup.text
soup_handled=remove_tags(soup_handle)
url_origin="https://account.google.com/signin/v2/indentfier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"

https://project.starinc.xyz/pbp_test/test.php
"""