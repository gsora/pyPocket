# This script return a json object containing all the saved link on the authorized account, but does not beautify it or nothing else.

import pyPocket
import os

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
    
# now let's see some data
gData = pyPocket.getData(consumerKey, aTok)
print(gData)
file.close()