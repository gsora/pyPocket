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

import requests
import json

def requestToken(consumerKey, redirectUri):
    methodURL = "https://getpocket.com/v3/oauth/request"
    parameters = {'consumer_key': consumerKey, 'redirect_uri': redirectUri}
    headers = {'content-type': 'application/json; charset=UTF-8'}
    pocket = requests.post(methodURL, data=json.dumps(parameters), headers=headers)
    requestToken = pocket.text[5:]
    return requestToken

def accessToken(consumerKey, requestToken):
    loginMethod = "https://getpocket.com/v3/oauth/authorize"
    parametersLogin = {'consumer_key': consumerKey, 'code': requestToken}
    headers = {'content-type': 'application/json; charset=UTF-8'}
    pocketLogin = requests.post(loginMethod, data=json.dumps(parametersLogin), headers=headers)
    accessToken = pocketLogin.text[13:43]
    return accessToken

def getData(consumerKey, accessToken):
    getDataMethod = "https://getpocket.com/v3/get"
    parametersGetData = {'consumer_key': consumerKey, 'access_token': accessToken}
    headers = {'content-type': 'application/json; charset=UTF-8'}
    getData = requests.post(getDataMethod, data=json.dumps(parametersGetData), headers=headers)
    
    # getData.text is a json object
    return getData.text

def addData(consumerKey, accessToken, URL):
    addDataMethod = "https://getpocket.com/v3/add"
    parametersAddData = {'consumer_key': consumerKey, 'access_token': accessToken, 'url': URL}
    headers = {'content-type': 'application/json; charset=UTF-8'}
    addData = requests.post(addDataMethod, data=json.dumps(parametersAddData), headers=headers)
    # TODO: not sure about this
    if(addData.text == "400 Bad Request"):
        raise AttributeError("Pocket returned Bad Request")
    else:
            return(addData.text)
