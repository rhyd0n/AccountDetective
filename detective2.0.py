import time 
import requests
import os
print("\033[0;31m"+'Welcome to AccFetcher')
acc=input("\033[0;31m"+'Enter the username you would like to search for. \n >> '+"\033[0m")
time.sleep(0.7)
os.system('clear')
print("\033[0;31m"+'Please wait a few seconds for the accounts to show up under this \n | \n V'+"\033[0m")
time.sleep(4)
a=requests.get('http://www.chess.com/member/'+acc)

if a.status_code == 200:
  print("\033[0;32m"+"[➤] chess.com: chess.com/members/"+acc)



c=requests.get("https://rive.app/"+acc)
print(c.status_code)
if c.status_code == 200:
  print("\033[0;32m"+'[➤] rive.app/'+acc)
 
d=requests.get("http://facebook.com/"+acc)

if d.status_code == 200:
  print("\033[0;32m"+'[➤] facebook.com/'+acc)
e=requests.get("http://reddit.com/user/"+acc)
if e.status_code == 200:
  print("\033[0;32m"+'[➤] reddit.com/user/'+acc)
'''
x=requests.get('http://site/'+acc)
if x.status_code == 200:
print("\003[0;32:"+'[➤] site/'+acc)
-- Template for other sites. 
 -- Please Please add more sites.
   -- Thanks. 
    -- Love, m000000000n
'''  
