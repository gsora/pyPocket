# This script return a json object containing all the saved link on the authorized account, but does not beautify it or nothing else.

import pyPocket
import os
import json
import time

consumerKey = "YOUR-CONSUMER-KEY"
redirectUri = "http://gsora.me"

if(not os.path.isfile("myLoginData")):
    # get the request token and authorize it

    rTok = pyPocket.requestToken(consumerKey, redirectUri)
    url = "Go to https://getpocket.com/auth/authorize?request_token={}&redirect_uri={} then press enter".format(rTok, redirectUri)
    print(url)
    a = input("")

    # then get the access token and save into a file

    aTok = pyPocket.accessToken(consumerKey, rTok)
    file = open("myLoginData", "r+")
    file.write(aTok)
    file.close()

file = open("myLoginData", "r+")
aTok = file.readline()
    
# now let's parse some data
gData = pyPocket.getData(consumerKey, aTok)

# load the json
pocketJson = json.loads(gData)

# print article id, title, url, date of add, word count, total entry

entryCounter = 0

for i in pocketJson["list"]:
    print("Pocket Item ID: {}".format(pocketJson["list"][i]["resolved_id"]))
    print("Article title: {}".format(pocketJson["list"][i]["resolved_title"]))
    print("Article URL: {}".format(pocketJson["list"][i]["resolved_url"]))
    print("Added the: {}".format(time.ctime(int(pocketJson["list"][i]["time_added"]))))
    print("Word count: {}\n\n".format(pocketJson["list"][i]["word_count"]))
    entryCounter+=1

print("JSON: {} item/s".format(entryCounter))

file.close()
