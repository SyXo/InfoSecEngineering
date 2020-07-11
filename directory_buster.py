#Python dirb (Web Content Scanner)

import requests


site = input("Site name to scan: ")
webReq = "http://www." + site + "/"

wordlist = input("Wordlist to use: ")

wordlistFile = open(wordlist, 'r')

print("These paths returned an HTTP status code of 200:")

for line in wordlistFile:
    
    line = line.strip()
    
    response = requests.get(webReq + line)

    if response.status_code == 200:
        print(site + "/" +  line)
