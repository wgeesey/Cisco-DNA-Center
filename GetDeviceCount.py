import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

USERNAME = input("Please enter your username: ")
PASSWORD = getpass("Please enter your password: ")

URL = "https://sandboxdnac.cisco.com"
authAPI = "/dna/system/api/v1/auth/token"
deviceCount = "/dna/intent/api/v1/network-device/count"

authPayload={}
authHeaders = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

dnaAuth = URL + authAPI

authResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=authHeaders, data=authPayload)

TokenJSON = authResponse.json()

Token = TokenJSON['Token']

#print('Your token was generated successfully. The token is:\n' + Token)#

dnaDeviceCount = URL + deviceCount

devCountPayload={}
devCountHeaders = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': Token
  }

devCountResponse = requests.get(dnaDeviceCount, headers=devCountHeaders, data=devCountPayload)

devCountJSON = devCountResponse.json()

print(devCountJSON)
