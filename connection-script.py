from urllib.request import urlopen
import os
import subprocess
import time

dir = "C:\speedtest.exe"



def internet_on():
   try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
   except: 
        return False
        

#while(internet_on()):
#    os.startfile(dir)
#    os.system(dir)
#    subprocess.Popen([dir])
#    subprocess.call(dir)
#    break
abcd=0
flag = 0
count = 0
while(True):
    if internet_on()==True:
        print(".", end="")
        time.sleep(1)
        if flag == 0:
            time.sleep(3)
            #os.startfile(dir)
            #os.system(dir)
            #subprocess.Popen([dir])
            subprocess.call(dir)
            flag = 1
            
        else:
            count = count + 1
            #print("skipping...")
            print(str(count), end="")
            continue
    else:
        print("no connection", end+"")
        flag = 0