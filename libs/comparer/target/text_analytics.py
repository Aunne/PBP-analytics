import requests
from bs4 import   BeautifulSoup

url_origin="https://project.starinc.xyz/pbp_test/test.php"
url_code=requests.get(url=url_origin).text
soup=BeautifulSoup(url_code,'lxml')

if 'bbb' in soup.title.string :
    print("yes")
else :
    for tag_input in soup.find_all('input') :
        if '登入' in tag_input.text :
            print('yes')
        else :
            print(tag_input.text)

    


"""
def remove_tags(code_handle) :
    return ''.join(xml.etree.ElementTree.fromstrig(soup_handle).itertext())

soup_handle=soup.text
soup_handled=remove_tags(soup_handle)
url_origin="https://account.google.com/signin/v2/indentfier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"

https://project.starinc.xyz/pbp_test/test.php
"""