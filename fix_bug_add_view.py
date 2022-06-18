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
        session = requests.Session()
        reg = session.post('https://api.mcontent.net/system/api/emailverification',json={"email":email,"password":"password123OK$$","type":"user"},headers=headers)
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
                    
                     
                    r = session.post('https://api.mcontent.net/system/api/newregistration',json={"otp":otp.strip(),"email":email,"pass":"password123OK$$","p_num":f"+6381932{random.randint(100000,999999)}","dob":"08/06/1999","gen":"Female","username":additonal,"type":"user","referral":"sophidwan77","wallet_id":"61b6f997c136e86dc9459492"},headers=headers)
                    try:
                        r = session.post('https://api.mcontent.net/system/api/newregistration',json={"otp":otp.strip(),"email":email,"pass":"password123OK$$","p_num":f"+6381932{random.randint(100000,999999)}","dob":"08/06/1999","gen":"Female","username":additonal,"type":"user","referral":"sophidwan77","wallet_id":"61b6f997c136e86dc9459492"},headers=headers)
                    except:
                        pass
                    r = json.loads(r.text)
                    sleep(3)
                    print(f"[*] [{email}] Verification {r['message']}!")
                    
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
            r = reds.post('https://proapi.mcontent.net/system/api/logincheck',json = {
            "email": email,
            "password": password
            },headers=header).text
            get_id = json.loads(r) 
            get_id = get_id['_id']['$oid']
            username = fake.first_name()+fake.last_name()+str(f"{random_angka_dua}").lower()
      
            r = reds.post('https://proapi.mcontent.net/system/api/profile',json={"id":get_id,"username":username,"fname":fake.first_name(),"lname":fake.last_name(),"p_num":"","dob":"","abt_me":"","lang":{"tag":"","tagsArray":[]},"work_data":[{"id":0,"name":"","website":"","occupation":"","from":"","to":"","datepickerV":'false',"datepickerT":'false'}],"pro_skills":{"tag":"","tagsArray":[]},"edu_data":[{"id":0,"type1":"","from":"","to":"","datepickerF":'false',"datepickerT":'false'}],"hob":{"tag":"","tagsArray":[]},"referal":"i1mam"},headers=header)

            # print(r.text)
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
                    
                    f.write(email+"|"+"password123OK$$"+"\n")
            else:
                print(f"[*] [{email}] Fill Data Not Success!")
            try:
                add_subs = reds.post('https://proapi.mcontent.net/system/api/videosubscribers',json = {
                    'attributes_type': '1',
                    'status': "1",
                    'subscriber_userid': get_id,
                    'userid': "6220f2b23d0125257a3f1942" #Change this userid your channel: https://mcontent.net/channel/6275168ec9168a7326305047 << CHANNEL ID
                },headers=header,timeout=10)
                add_subs = add_subs.text
    
                if '"success":1' in add_subs:
                    print(f"[*] [{email}] Success Subscribe")
                else:
                    print(f"[*] [{email}] Failed Subscribe")
            except:
                print(f"[*] [{email}] Failed Subscribe: API Subscribe is OFFLINE by Developer!")
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
           
            headers = {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
                "cache-control": "no-cache",
                "content-type": "application/json",
                "pragma": "no-cache",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "Referer": "https://mcontent.net/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            } 
            
            check_vid = reds.get('https://mcontent.net/video/6278cdeb0136e910893386b4',headers=headers, stream=True).text
    
            
            video_userid = check_vid.split(r'<a class="channelname" href="https://mcontent.net/channel/')[1].split(r'" >  <img class="img-fluid"')[0]
 
            insert_views = reds.post('https://proapi.mcontent.net/system/api/insertviews',json = {
                            "video_id": "6278cdeb0136e910893386b4", #Change this video_id your channel: https://mcontent.net/video/6278cdeb0136e910893386b4 << VIDEO ID
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
