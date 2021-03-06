'''
    The MIT License (MIT)
    Copyright (c) 2014 PeppeLaKappa
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
    OR OTHER DEALINGS IN THE SOFTWARE.
'''

# This script return a json object containing all the saved link on the authorized account, but does not beautify it or nothing else.

import pyPocket
import os
import json
import time
import argparse

# initialize the argparse
parser = argparse.ArgumentParser()
parser.add_argument("--getLinks", help="get the list of the authorized account's saved links", action="store_true")
parser.add_argument("--add", help="add a link to the authorized account")
args = parser.parse_args()

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

if args.getLinks:
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
if args.add:
    print("Working...")
    try:
        pyPocket.addData(consumerKey, aTok, args.add)
        print("Added!")
    except AttributeError:
        print("Failed!")

file.close()
