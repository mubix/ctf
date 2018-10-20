# Code by
# Kelly Lehman
# @r3curs3
# 10/19/2018

import requests
from multiprocessing.dummy import Pool as ThreadPool
requests.packages.urllib3.disable_warnings()

url = "https://pickanumber.h4110w33n.com/"

payloads = []

for x in range(0,10001):
    payloads.append(x)

def worker(payload):
    #print(str(payload))
    r = requests.get(url+str(payload)+".html")
    if "Not what" not in r.text:
        print(str(payload), r.text)

pool = ThreadPool(200)
results = pool.map(worker, payloads)
pool.close()
pool.join()
