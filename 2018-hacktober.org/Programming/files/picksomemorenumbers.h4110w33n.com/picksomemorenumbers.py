# Code by
# Kelly Lehman
# @r3curse
# 10/19/2018

import pyotp
import requests

url = "https://picksomemorenumbers.h4110w33n.com/"
requests.packages.urllib3.disable_warnings()

key = pyotp.TOTP('YSH45EYF35IRJHVV').now()
r = requests.post(url, data={"number1":key[0:3]}, verify=False)
r = requests.post(url+r.history[0].headers['location'], data={"number2":key[3:]}, verify=False)
print(r.text)
