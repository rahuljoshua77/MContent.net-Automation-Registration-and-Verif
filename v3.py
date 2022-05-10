from webbrowser import get
import requests,random,json,os, time,string
cwd = os.getcwd()
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
fake = Faker() 
# brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver_path= f"{cwd}\\chromedriver.exe"
firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')

firefox_options.headless = False
firefox_options.add_argument('--disable-setuid-sandbox')
firefox_options.add_argument('disable-infobars')
firefox_options.add_argument('--ignore-certifcate-errors')
firefox_options.add_argument('--ignore-certifcate-errors-spki-list')
firefox_options.add_argument("--incognito")
firefox_options.add_argument('--no-first-run')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--disable-infobars")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-popup-blocking")
firefox_options.add_argument('--log-level=3')

firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_experimental_option("useAutomationExtension", False)
firefox_options.add_experimental_option("excludeSwitches",["enable-automation"])
firefox_options.add_experimental_option('excludeSwitches', ['enable-logging'])
firefox_options.add_argument('--disable-notifications')
from selenium.webdriver.common.action_chains import ActionChains
# firefox_options.binary_location = brave_path
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)

def sign_up(k):
    password = "1234567Ok**"
    additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    email = str(additonal)+str(additonal)+"@tafmail.com"
    try:
        
        k = k
        
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "id-ID,id;q=0.9",
            "content-type": "application/json",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "cookie": "PHPSESSID=36f1m1v9mp5jo3i924nc92hvs2",
            "Referer": "https://mcontent.net/portal/home",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        } 
      
        reg = requests.post('https://mcontent.net/register',json={
                "email": email,
                "pass": password
                },headers=headers)
        
        n = 1
        while True:
            sleep(2)
            if n == 10:
                print("[*] Verification Failed!")
                break
            URL = f'https://getnada.com/api/v1/inboxes/{email}'
            
            r = requests.get(URL).json()
            #getting the latest message
    
            try:
                global uid
                
                uid = r['msgs'][0]['uid']
            
                mes = requests.get(f'https://getnada.com/api/v1/messages/html/{uid}')
                mes1 = BeautifulSoup(mes.content,'html.parser')
                get_data = mes1.prettify()
                
                get_data = get_data.split('''Follow this link to verify your email address''')
                get_data = get_data[1].split('https://mcontent-aaae9.firebaseapp.com/__/auth/action?mode=verifyEmail&amp;oobCode=')
                
                get_data = get_data[1].split('''" target="_blank">''')
                
                get_data = get_data[0]
                url_activation = f"https://mcontent-aaae9.firebaseapp.com/__/auth/action?mode=verifyEmail&amp;oobCode={get_data}"
                code_active = url_activation.replace(";","&").replace('https://mcontent-aaae9.firebaseapp.com/__/auth/action?mode=verifyEmail&amp&oobCode=','').replace('&amp&apiKey=AIzaSyCYGucEjNqTDQ7JUgDT9G7aqG9nT-FD1tI&amp&lang=en','').strip()
                print(f'[*] [{email}] Code Activation: {code_active}')
                
                headers={
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
                    "cache-control": "no-cache",
                    "content-type": "application/json",
                    "pragma": "no-cache",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site",
                    "x-client-data": "CIm2yQEIprbJAQjEtskBCKmdygEIkqHLAQin+csBCOaEzAEIgp3MAQiIq8wB",
                    "x-client-version": "Chrome/JsCore/3.7.5/FirebaseCore-web",
                    "Referer": "https://mcontent-aaae9.firebaseapp.com/",
                    "Referrer-Policy": "strict-origin-when-cross-origin"
                }#https://mcontent-aaae9.firebaseapp.com/__/auth/action?mode=verifyEmail&oobCode=hdgzTvVZXeiWPX6AqofYRr5hkXKSox_0cnwAC2IMQDgAAAGAq-tLfA&apiKey=AIzaSyCYGucEjNqTDQ7JUgDT9G7aqG9nT-FD1tI&lang=en
                r = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/setAccountInfo?key=AIzaSyCYGucEjNqTDQ7JUgDT9G7aqG9nT-FD1tI',json={"oobCode":code_active},headers=headers)
                r = json.loads(r.text)
                sleep(3)
                print(f"[*] [{email}] Verification {r['emailVerified']}!")
                
                with open('ress.txt','w') as f:
                    f.write(f"{email}|{password}\n")
                break
            except Exception as e:
                print(e)
                print(f"[*] [{email}] Your Email doesn't have a new message, Reload!")
                n = n+1
             

        header = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "id-ID,id;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://mcontent.net/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        reds = requests.Session()
        r = reds.post('https://proapi.mcontent.net/system/api/logincheck',json = {
        "email": email,
        "password": password
        },headers=header).text
        get_id = json.loads(r) 
        get_id = get_id['_id']['$oid']
        username = fake.first_name()+fake.last_name()+str(f"{random_angka_dua}").lower()
    
        r = reds.post('https://proapi.mcontent.net/system/api/profile',json={"id":get_id,"username":username,"fname":fake.first_name(),"lname":fake.last_name(),"p_num":"","dob":"","abt_me":"","lang":{"tag":"","tagsArray":[]},"work_data":[{"id":0,"name":"","website":"","occupation":"","from":"","to":"","datepickerV":'false',"datepickerT":'false'}],"pro_skills":{"tag":"","tagsArray":[]},"edu_data":[{"id":0,"type1":"","from":"","to":"","datepickerF":'false',"datepickerT":'false'}],"hob":{"tag":"","tagsArray":[]},"referal":"i1mam"},headers=header)

        
        additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        headers= {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "pragma": "no-cache",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "Referer": "https://mcontent.net/",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        } 
        r = reds.post('https://proapi.mcontent.net/system/api/userwallet',json = {
                "userid": get_id,
                "wallet_id": "61b6f997c136e86dc9459492",
                "wallet_address": f"{str(additonal)}{str(additonal)}",
                "status": "active"
        },headers=header) 
        
    
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "pragma": "no-cache",
            "sec-ch-ua": "\"\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "Referer": "https://mcontent.net/",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        
        add_data = reds.post('https://proapi.mcontent.net/system/api/profile',json = {
            "uploadtype": "shortedit",
            "id": get_id,
            "fname": fake.first_name(),
            "lname": fake.last_name(),
            "dob": f"{random.randint(1990,1999)}-0{random.randint(1,9)}-0{random.randint(1,9)}",
            "abt_me": str(additonal),
            "gen": "Male"
            },headers=headers)
        if str(add_data.text) == "1":
            print(f"[*] [{email}] Fill Data Success!")
            with open('acc.txt','a') as f:
                
                f.write(email+"|"+password+"\n")
        else:
            print(f"[*] [{email}] Fill Data Not Success!")
    except Exception as e:
        print(f"[*] [{email}] Error: {e}")
    
 
    
if __name__ == '__main__':
 
    global password
    print("[*] Auto Creator MContent")
    jumlah = input("[*] Multiprocessing: ")
    loop_input = int(input("[*] How Much Account: "))
    loop = []
    for i in range(1, loop_input+1):
        loop.append(i)
    
    start = time.time()
    with Pool(int(jumlah)) as p:  
        p.map(sign_up, loop)
      
            
    end = time.time()
    print("[*] Time elapsed: ", end - start)
