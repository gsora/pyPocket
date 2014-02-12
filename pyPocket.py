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
    return addData.text
