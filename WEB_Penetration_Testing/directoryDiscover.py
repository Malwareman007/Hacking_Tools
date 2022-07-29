#/usr/bin/python


import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

targetURL = input("Enter Target URL: ")
file = open("common.txt", "r")
for line in file:
    line = line.strip('\n')
    fullURL = targetURL + "/" + line
    response = request(fullURL)
    if response:
        print('[+] Discovered Directory at Link: ' + fullURL)
