from webbrowser import get
import requests,random,json,os, time,string
cwd = os.getcwd()
from bs4 import BeautifulSoup
from time import sleep
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from requests_html import HTMLSession

session = HTMLSession()
def login(data):
    data = data.split("|")
    email = data[0]
    passwords = data[1]
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "pragma": "no-cache",
        "sec-ch-ua": "\"\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://pltplace.io/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    login_acc = requests.Session()
    reg = login_acc.post('https://api.pltplace.io/api/v1/account/login',json={
                "email": email,
                "password": passwords
                },headers=headers)
 
    reg = login_acc.post('https://api.pltplace.io/api/v1/account/email/activate',headers=headers)
    print(f"[*] [{email}] Login")
    repeat = 1
    while True:
        if repeat == 5:
            print(f"[*] [{email}] Verification Failed")
            break
        try:
            print(f"[*] [{email}] Checking email...")
            check_mail(email,login_acc)
            break
        except:
            repeat = repeat + 1
            
def check_mail(email,login_acc):
    header_check = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "sec-ch-ua": "\"\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "",
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://tempmail.plus/en/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    email = email.replace("@",'%40')
    get_mail = requests.get(f'https://tempmail.plus/api/mails?email={email}&limit=20&epin=',headers=header_check)
    get_mail = get_mail.json()
    id_mail = get_mail['last_id']
    print(id_mail)
    
    headers={
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "cookie": "email=MargaretRansom1682%40tofeat.com",
        "Referer": "https://tempmail.plus/en/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    get_mail = requests.get(f'https://tempmail.plus/api/mails/{id_mail}?email={email}&epin=',headers=headers,stream=True)
    mes1 = BeautifulSoup(get_mail.content,'html.parser')
    get_data = mes1.prettify()
    get_data = get_data.replace("\\",'').split('nnhttps://pltplace.io/email_active?activate_code=')[1].split('nn本リンクの有効期限は')[0]
 
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    print(f'[{email}] URL Verification: https://pltplace.io/email_active?activate_code={get_data}')
    req = session.get(f'https://pltplace.io/email_active?activate_code={get_data}')
    #print(req.text)
    req.html.render()  
  
    print(f"[*] [{email}] Verification success")

def main():
    print(f"[*] Auto verifikasi")
    myfile = open(f"{cwd}\\list.txt","r")
    list_account = myfile.read()
    list_accountsplit = list_account.split("\n")
    for i in list_accountsplit:
        login(i)
