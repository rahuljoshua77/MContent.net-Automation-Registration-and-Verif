from webbrowser import get
import requests,random,json,os, time,string
cwd = os.getcwd()
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from multiprocessing import Pool
from time import sleep
from faker import Faker
fake = Faker() 
  
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)

def sign_up(k):
    password = "1234567Ok**"
    additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    email = fake.first_name()+fake.last_name()+"@getnada.com"
    email = email.lower()
    try:
        
        k = k
    
        headers= {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "pragma": "no-cache",
            "sec-ch-ua": '"\"\""',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "cookie": "PHPSESSID=o9ua6186tqh7opjnu6f57ksjoa",
            "Referer": "https://mcontent.net/home",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        } 
        reg = requests.post('https://mcontent.net/register',json={
                "email": email,
                "pass": password
                },headers=headers)
        reg = reg.json()
 
        if reg['msg'] == "Register successfully.":
            print(f"[*] [{email}] {reg['msg']}")
            status_reg = "True"
        else:
            print(f"[*] [{email}] {reg['msg']}")
            status_reg = "False"
        if status_reg == "True":
            n = 1
    
            while True:
                sleep(5)
                if n == 5:
                    print(f"[*] [{email}]  Verification Failed!")
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
                    "wallet_address": f"0x7e3fb0c1ae8e{additonal}124c747cf8da9fd357{additonal}",
                    "status": "active"
            },headers=header)
 
            if "1" in str(r.text):
                print(f"[*] [{email}] Add Address Success!")
                 
            else:
                print(f"[*] [{email}] Add Address Not Success!")
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

            add_subs = reds.post('https://proapi.mcontent.net/system/api/videosubscribers',json = {
                'attributes_type': '1',
                'status': "1",
                'subscriber_userid': get_id,
                'userid': "6220f2b23d0125257a3f1942" #Change this userid your channel: https://mcontent.net/channel/6275168ec9168a7326305047 << CHANNEL ID
            },headers=header)
            add_subs = add_subs.text
    
            if '"success":1' in add_subs:
                print(f"[*] [{email}] Success Subscribe")
            else:
                print(f"[*] [{email}] Failed Subscribe")
            add_like = reds.post('https://proapi.mcontent.net/system/api/videoattributes',json = {
                'attributes_type': '1',
                'status': "1",
                'video_id': "6278cdeb0136e910893386b4", #Change this video_id your channel: https://mcontent.net/video/6278cdeb0136e910893386b4 << VIDEO ID
                'userid': get_id, 
                'video_type': "mbrowse"
            },headers=header)
            add_like = add_like.text
            if '"success":1' in add_like:
                print(f"[*] [{email}] Success Like")
            else:
                print(f"[*] [{email}] Failed Like")
            
        else:
            print(f"[*] [{email}] Registery Not Success!")
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
