import time 
import requests
print('Welcome to AccFetcher')
acc=input('Enter the username you would like to search for. \n >> ')
print('Please wait a few seconds for the accounts to show up under this \n | \n V')
time.sleep(4)
a=requests.get('http://www.chess.com/member/'+acc)

if "Oops!" not in a.text:
  print("[➤] chess.com: chess.com/members/"+acc)

b=requests.get("http://youtube.com/c/"+acc)

if "This page isn't available" not in b.text:
  print('[➤] youtube.com: youtube.com/c/'+acc)

c=requests.get("http://twitter.com/"+acc)

if "This account doesn’t exist" not in c.text:
  print('[➤] twitter.com/'+acc)
  
d=requests.get("http://facebook.com/"+acc)

if "This page isn't available" not in d.text:
  print('[➤] facebook.com/'+acc)
