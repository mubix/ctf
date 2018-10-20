# Code by
# Kelly Lehman
# @r3curs3
# 10/19/2018

import pyotp
from datetime import datetime, date, timedelta
import calendar
import json
import requests
from html.parser import HTMLParser

def get_time(tmp):
    time = tmp.split()
    month = dict((v,k) for k,v in enumerate(calendar.month_abbr))[time[4].strip(' ,')[0:3]]
    delta = time[8].strip(' ,').split(":")
    t = timedelta(hours=int(delta[0])-6, minutes=int(delta[1]), seconds=int(delta[2]))
    return datetime(int(time[6]), month, int(time[5].strip(' ,'))) + t

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.time = ""

    def handle_data(self, data):
        if self.get_starttag_text() == "<h3>":
            if data.strip() == "":
                return
            self.time = data.strip().lstrip(' -\n\r').rstrip(' -\n\r')
            #print("handle_data:", self.time)

parser = MyHTMLParser()
url = "https://numbersthroughtime.h4110w33n.com/"
requests.packages.urllib3.disable_warnings()
parser.feed(requests.get(url, verify=False).text)

key = pyotp.TOTP('CI4V2HKDLMFZBKAY').at(get_time(parser.time))
r = requests.post(url, data={"number1":key[0:3]}, verify=False)
r = requests.post(url+r.history[0].headers['location'], data={"number1":key[3:]}, verify=False)
print(r.text)
