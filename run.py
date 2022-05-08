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

firefox_options.headless = True
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
 
def xpath_el(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))

    return browser.execute_script("arguments[0].click();", element_all)

def xpath_ex(el):
    element_all = wait(browser,0.3).until(EC.presence_of_element_located((By.XPATH, el)))
    browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_id(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'//input[@{el}]'))).send_keys(word)

def sign_up(k):
    try:
        global browser
        k = k
        
        prefix_email = prefix.split("@")
        get_mail = prefix_email[1]
        get_user = prefix_email[0]
        additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        email = get_user+f"{k}"+additonal+"@"+get_mail
        file_list_akun = "password.txt"
        myfile_akun = open(f"{cwd}/{file_list_akun}","r")
        password = myfile_akun.read()
        
        # firefox_options.add_experimental_option('w3c', False)
        #firefox_options.add_experimental_option("mobileEmulation", mobile_emulation)
        firefox_options.add_argument(f"user-agent=Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1")
        browser = webdriver.Chrome(options=firefox_options,executable_path=driver_path)
        browser.execute_script("document.body.style.zoom='zoom 90%'")
        browser.get('https://mcontent.net/register')
        print(f"[+] [{email}] Trying to Creating New Account...!")
        
        email_input = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="Email"]')))
        email_input.send_keys(email)
        sleep(1)
        password_input = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@name="Password"]')))
        password_input.send_keys(password)
        sleep(1)
        password_input = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@id="formBasicRetypePassword"]')))
        password_input.send_keys(password)
        sleep(1)
        wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@type="checkbox"]'))).click()
        
        xpath_el('//button[@type="submit"]') 
        sleep(5)
        n = 1
        print(f"[*] [{email}] Please wait!")
        
        while True:
            
            if n == 5:
                print("[*] Verification Failed!")
                break
            URL = f'https://getnada.com/api/v1/inboxes/{email}'
            r = requests.get(URL).json()
            #getting the latest message
    
            try:
                global uid
                sleep(1)
                uid = r['msgs'][0]['uid']
            
                mes = requests.get(f'https://getnada.com/api/v1/messages/html/{uid}')
                mes1 = BeautifulSoup(mes.content,'html.parser')
                get_data = mes1.prettify()
                
                get_data = get_data.split('''Follow this link to verify your email address''')
                get_data = get_data[1].split('https://mcontent-aaae9.firebaseapp.com/__/auth/action?mode=verifyEmail&amp;oobCode=')
                
                get_data = get_data[1].split('''" target="_blank">''')
                
                get_data = get_data[0]
                url_activation = f"https://mcontent-aaae9.firebaseapp.com/__/auth/action?mode=verifyEmail&amp;oobCode={get_data}"
                print(f'[*] URL Activation: {url_activation.replace(";","&")}')
                
                browser.get(url_activation.replace(";","&"))
                sleep(3)
                print(f"[*] [{email} Verification Success!")
                
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
    
        if str(r.text) == "1":
            print(f"[*] [{email}] Fill Data Success!")
            with open('acc.txt','a') as f:
                f.write(email+"|"+password+"\n")
        else:
            print(f"[*] [{email}] Fill Data Not Success!")
    except Exception as e:
        print(f"[*] [{email}] Error: {e}")
    
    browser.quit()
    
if __name__ == '__main__':
    global prefix
    global password
    print("[*] Auto Creator MContent")
    prefix = str(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5)))+"@getnada.com"
 
    password = "tesPasWord123@@"
   
    loop_input = int(input("[*] How Much Account: "))
    start = time.time()
    for i in range(0,loop_input):
        sign_up(i)
      
            
    end = time.time()
    print("[*] Time elapsed: ", end - start)