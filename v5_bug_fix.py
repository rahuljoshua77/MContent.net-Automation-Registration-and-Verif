from email import message
from requests_html import HTMLSession

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
    reds = requests.Session()
    password = "password123OK$$"
    additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    email = fake.first_name()+fake.last_name()+str(random_angka)+"@getnada.com"
    email = email.lower()
    try:
        
        k = k
    
        headers= {
        'Host': 'api.mcontent.net',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '213',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.9.1'
        } 
         
        reg = reds.post('https://api.mcontent.net/system/api/emailverification',json={"email":email,"password":"password123OK$$","type":"user"},headers=headers)
        reg = reg.json()
 
        if "code sent" in str(reg['message']):
            print(f"[*] [{email}] {reg['message']}")
            status_reg = "True"
        else:
            print(f"[*] [{email}] {reg['message']}")
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
                
                    
                    #text = '<h2 style="background: #ffdf00;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">9166</h2>'

                    otp = get_data.split(r'width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">')[1].split('</h2>')[0]
                    print(f'[*] [{email}] Code OTP: {otp.strip()}')
                    
                     
                    r = reds.post('https://api.mcontent.net/system/api/newregistration',json={"otp":otp.strip(),"email":email,"pass":"password123OK$$","p_num":f"+6381133{random.randint(100000,999999)}","dob":"08/06/1999","gen":"Female","username":additonal,"type":"user","referral":"Minuman","wallet_id":"61b6f997c136e86dc9459492"},headers=headers)
                    try:
                        r = reds.post('https://api.mcontent.net/system/api/newregistration',json={"otp":otp.strip(),"email":email,"pass":"password123OK$$","p_num":f"+6381133{random.randint(100000,999999)}","dob":"08/06/1999","gen":"Female","username":additonal,"type":"user","referral":"Minuman","wallet_id":"61b6f997c136e86dc9459492"},headers=headers)
                    except:
                        pass
                    r = json.loads(r.text)
                    sleep(3)
                    print(f"[*] [{email}] Verification  success!")
                    
                    with open('ress.txt','a') as f:
                        f.write(f"{email}|password123OK$$\n")
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
            r = reds.post('https://api.mcontent.net/system/api/userlogincheck',json = {
            "email": email,
            "pass": "password123OK$$"
            },headers=header).json()
            print(f"[*] [{email}] {r['message']}")
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
                     
                    
                    uid = r['msgs'][0]['uid']
                
                    mes = requests.get(f'https://getnada.com/api/v1/messages/html/{uid}')
                    mes1 = BeautifulSoup(mes.content,'html.parser')
                    get_data = mes1.prettify()
                
                    
                    #text = '<h2 style="background: #ffdf00;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">9166</h2>'

                    new_otp = get_data.split(r'width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">')[1].split('</h2>')[0]
                    print(f'[*] [{email}] Code OTP: {new_otp.strip()}')
                    if new_otp == otp:
                        pass
                    else:
                         
                        headers = {
                            "accept": "application/json, text/javascript, */*; q=0.01",
                            "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
                            "content-type": "application/json",
                            "sec-ch-ua": "\"\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-ch-ua-platform": "",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "x-requested-with": "XMLHttpRequest",
                            
                            "Referer": "https://mcontent.net/home",
                            "Referrer-Policy": "strict-origin-when-cross-origin"
                        } 
                        r = reds.post('https://mcontent.net/logindata',json={"email":email, "otp":new_otp.strip(),"pass":password},headers=headers).json()
                 
                        with open('ress.txt','a') as f:
                            f.write(f"{email}|password123OK$$\n")
                        break
                    
                        
                except:
                    n = n+1
                    pass
            
            username = fake.first_name()+fake.last_name()+str(f"{random_angka_dua}").lower()
   
            get_id = r['data']['userid']
             
            additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
            headers = {
                        "accept": "*/*",
                        "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
                        "authorization": f"Bearer {r['bearer']}",
                        "content-type": "application/json",
                        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "Referer": "https://mcontent.net/",
                        "Referrer-Policy": "strict-origin-when-cross-origin"
                    } 
            r = requests.post('https://api.mcontent.net/system/api/userwallet',json = {
                    "userid": get_id,
                    "wallet_id": "61b6f997c136e86dc9459492",
                    "wallet_address": f"0x7e3fb0c1ae8e{additonal}124c747cf8da9fd357{additonal}",
                    "status": "active"
            },headers=headers)
             
            if "1" in str(r.text):
                print(f"[*] [{email}] Add Address Success!")
                 
            else:
                print(f"[*] [{email}] Add Address Not Success!")
             
            
            add_data = requests.post('https://api.mcontent.net/system/api/profile',json =
                {"uploadtype":"shortedit","fname":"rahul","lname":"joshua","dob":"1992-04-22","abt_me":"asdasdasd","gen":"Female"},headers=headers)
            # if str(add_data.text) == "1":
            #     print(f"[*] [{email}] Fill Data Success!")
            #     with open('acc.txt','a') as f:
                    
            #         f.write(email+"|"+"password123OK$$"+"\n")
            # else:
            #     print(f"[*] [{email}] Fill Data Not Success!")
            try:
                add_subs = requests.post('https://api.mcontent.net/system/api/videosubscribers',json = {
                    #{"attributes_type":"1","status":"1","userid":"6273c5306a8383194d409399","subscriber_userid":"62daaf30dd34e550d555dd18"}
                    'attributes_type': '1',
                    'status': "1",
                    'subscriber_userid': get_id,
                    'userid': "6273c5306a8383194d409399" #Change this userid your channel target:https://mcontent.net/channel/62daaf30dd34e550d555dd18 << CHANNEL ID
                },headers=headers,timeout=10).json()
         
              
                
                if add_subs['message'] == "Inserted Successfully":
                    print(f"[*] [{email}] Success Subscribe")
                else:
                    print(f"[*] [{email}] Failed Subscribe")
            except:
                
                print(f"[*] [{email}] Failed Subscribe: API Subscribe is OFFLINE by Developer!")
            try:
                add_like = requests.post('https://api.mcontent.net/system/api/videoattributes',json =
                                    {"attributes_type":1,
                                    "status":"1",
                                    "video_id":"629f93dba54f140aea3143f8",
                                    "userid":get_id,
                                    "video_type":"mbrowse"},headers=headers).json()
             
                if add_data['results'][0]['message'] == "Inserted Successfully":
                    print(f"[*] [{email}] Success Like")
                else:
                    print(f"[*] [{email}] Failed Like")
            except Exception as e:
                if "Inserted Successfully" in str(e):
                    print(f"[*] [{email}] Success Like")
                else:
                    print(f"[*] [{email}] Failed Like")
             
            
            check_vid = reds.get('https://mcontent.net/video/629f93dba54f140aea3143f8',headers=headers, stream=True).text
    
            
            video_userid = check_vid.split(r'<a class="channelname" href="https://mcontent.net/channel/')[1].split(r'" >  <img class="img-fluid"')[0]
            video_userid  = video_userid.split('"> <img class="img-fluid"')[0]
            
            insert_views = requests.post('https://api.mcontent.net/system/api/insertviews',json = {
                            "video_id": "629f93dba54f140aea3143f8", #Change this video_id your channel: https://mcontent.net/video/6278cdeb0136e910893386b4 << VIDEO ID
                            "views": "1",
                            "wallet_id": "",
                            "video_userid": video_userid,
                            "transaction_type": "view",
                            "userid": get_id,
                            "video_type": "mbrowse"
                            },headers=headers).text
            
            print(f"[*] [{email}] Add View!")
        else:
            print(f"[*] [{email}] Registery Not Success!")
    except Exception as e:
        if str(e) == "Expecting value: line 1 column 1 (char 0)":
            pass
        else:
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
