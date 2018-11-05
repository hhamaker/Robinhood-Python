import requests
import json
import RobinhoodCredentials

class loginResonse(object):
    def __init__(self, backup_code, access_token, expires_in, mfa_code, token_type, scope, refresh_token):
        self.access_token = access_token
        self.backup_code = backup_code
        self.expires_in = expires_in
        self.mfa_code = mfa_code
        self.token_type = token_type
        self.scope = scope
        self.refresh_token = refresh_token

#makes a get call to robinhood quotes to get the stock info
def getloginToken():
    userName = RobinhoodCredentials.getUserName()
    password = RobinhoodCredentials.getPassword()
    clientId = RobinhoodCredentials.getClientId()
    grantType = RobinhoodCredentials.getGrantType()
    url = 'https://api.robinhood.com/oauth2/token/'
    content = requests.post(url, data = {'client_id':clientId, 
        'grant_type':grantType, 'username':userName, 'password':password})
    response = json.loads(content.text)
    return response["access_token"]

    #makes a get call to robinhood quotes to get the stock info
def getloginToken2():
    userName = RobinhoodCredentials.getUserName()
    password = RobinhoodCredentials.getPassword()
    url = 'https://api.robinhood.com/api-token-auth/'
    content = requests.post(url, data = {'username':userName, 'password':password})
    print(content.text)
    response = json.loads(content.text)
    return response["access_token"]

def logOut(token):
    url = 'https://api.robinhood.com/api-token-logout/'
    content = requests.post(url, headers = {"Authorization":"Token " + token})
    print("Logged Out.")
    return content

def migrateToken(token):
    url = 'https://api.robinhood.com/oauth2/migrate_token/'
    content = requests.post(url, headers = {"Authorization":"Token " + token})
    response = json.loads(content.text)
    return response["access_token"]

class migrateResonse(object):
    def __init__(self, token_type, access_token, expires_in, refresh_token, scope):
        self.token_type = token_type
        self.access_token = access_token
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.scope = scope
