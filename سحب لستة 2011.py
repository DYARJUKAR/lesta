import requests,random
from time import time
from user_agent import generate_user_agent
import secrets
import json
import time
import os
import threading
from threading import Thread
from faker import Faker
from concurrent.futures import ThreadPoolExecutor
import datetime,sys
import sys as n
import threading
import time as mm
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)
#print(t)

hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2024, 4,21, 00, 00 ,0) 

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print('\x1b[1;37m'' - تــم تـوقــيـف الاداة للاشــــــتراك - @OO272 - ')
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print('\x1b[1;37m'' - تــم تـوقــيـف الاداة للاشــــــتراك - @OO272 - ')
    print('\n\n')
    print(x)
    
    sys.exit(0)
O = '\x1b[38;5;208m' #برتقالي
Z = '\033[1;31m' #احمر
E = '\033[1;31m'
M = '\x1b[1;37m' 
m=0
ab=0
ids=[]
def uu():
  zan=int("".join(random.choice('7')for i in range(1)))
  re="".join(random.choice('1234567890')for i in range(zan))
  if re not in ids:
    ids.append(re)
    return re
  else:
    uu()
def username():
  global m
  try:
    while True:
      re=uu()
      csrftoken = secrets.token_hex(32)
      mmidd=secrets.token_hex(27)
      ig_=secrets.token_hex(36)
      datrr=secrets.token_hex(24)
      faker = Faker()
      fak = faker.user_agent()
      app=''.join(random.choice('936619743392459')for i in range(15))
      cookies = {
    'csrftoken': csrftoken,
    'ps_l': '0',
    'ps_n': '0',
    'ig_did': f'{ig_}',
    'ig_nrcb': '1',
    'dpr': '2.1988937854766846',
    'mid': mmidd,
    'datr': datrr,
}

      headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'csrftoken=GpSFJXM8cw5Ridi72oRh18; ps_l=0; ps_n=0; ig_did=BFD5A6E1-D993-48EE-914E-A6A5A2CC8D6D; ig_nrcb=1; dpr=2.1988937854766846; mid=ZhLiHgAEAAE63kJS7yz7sG6sp5mw; datr=HuISZrdPWEfDXxhdMTlBClqV',
    'dpr': '2.19889',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/a_1_in/?igsh=czFtZ3o1aDhraG01',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fak,
    'viewport-width': '891',
    'x-asbd-id': '129477',
    'x-csrftoken': csrftoken,
    'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
    'x-fb-lsd': 'AVoRhvRPoRs',
    'x-ig-app-id': app,
}

      data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '1',
    '__hs': '19820.HYP:instagram_web_pkg.2.1..0.0',
    'dpr': '2',
    '__ccg': 'UNKNOWN',
    '__rev': '1012604142',
    '__s': 'dmjo05:l5d6wo:20s0u7',
    '__hsi': '7355192092986103751',
    '__dyn': '7xeUjG1mxu1syUbFp40NonwgU29zEdF8aUco2qwJw5ux609vCwjE1xoswaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2swaO4U2zxe2GewGwso88cobEaU2eUlwhEe87q7U88138bpEbUGdwtU662O0Lo6-3u2WE5B0bK1Iwqo5q1IQp1yUoxe4UrAwCAxW6U',
    '__csr': 'gVb2snsIjkIQyjRmBaFGECih59Fb98nQBzbZ2IN8BqBGl7h9Am4ohAAD-vGBh4GizA-4aAiJ2vFDUR3qx596AhrBgzJlBKmu6VHiypryUkByrGiicgPAx6iUpGEOmqfykFA4801kXEkOwmU1Tqwvk8wCix64E0b_EaWdguwozat2F61-wiokxG0d9w2MFU5Kzo0k6wiU7Kut2F601_Ew1me',
    '__comet_req': '7',
    'lsd': 'AVoRhvRPoRs',
    'jazoest': '21036',
    '__spin_r': '1012604142',
    '__spin_b': 'trunk',
    '__spin_t': '1712514108',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
    'variables': '{"id":"'+re+'","relay_header":false,"render_surface":"PROFILE"}',
    'server_timestamps': 'true',
    'doc_id': '7381344031985950',
}

      response = requests.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data).json()
      rr = response['data']['user']['username']
      print(f'«{O}{rr}»')
      with open('username.txt','a') as zaid:
      	zaid.write(f'{rr}\n')      	
  except:
  	username()
with ThreadPoolExecutor(max_workers=50) as executor:
      futures = [executor.submit(username) for _ in range(50)]
      for future in futures:
      	future.result()