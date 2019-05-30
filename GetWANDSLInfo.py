#!/usr/local/bin/python3
 
import requests
import json
import argparse

parser = argparse.ArgumentParser(description="Retrieve JSON formatted WAN information from a Zytel PK5001Z modem")
parser.add_argument("host", help="DSL modem hostname/IP address")
parser.add_argument("user", help="DSL modem user name")
parser.add_argument("pw", help="DSL modem password")
parser.add_argument("-v", "--verbose", help="verbose prints debug information", action="store_true")

args = parser.parse_args()

login_url = 'http://'+args.host+'/login.cgi'
payload = {'loginSubmitValue':'1','admin_username':args.user,'admin_password':args.pw}
data_url = 'http://'+args.host+'/GetWANDSLInfo.cgi'
 
j = {'download':'0','upload':'0','dslStatus':'','internetStatus':'','modemIP':'','RemoteIP':''}

s = requests.Session()
resp = s.post(login_url, data=payload)
if resp.status_code == 200:
    if args.verbose:
        print (resp.status_code)
        print (resp.text)
    data = s.get(data_url)
    if data.status_code == 200:
        if args.verbose:
            print (data.status_code)
            print (data.text)
       
        values = data.text.split('|')
        if args.verbose:
            print (values)
        
        j['download'] = values[34]
        j['upload'] = values[32]
        j['dslStatus'] = values[30]
        j['internetStatus'] = values[0]
        j['modemIP'] = values[20]
        j['RemoteIP'] = values[26]

print (json.dumps(j))
