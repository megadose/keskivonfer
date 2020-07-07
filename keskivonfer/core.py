import requests
from fake_useragent import UserAgent
def getInfo(username,vintedExtension="com"):
    if vintedExtension==None:
        vintedExtension="com"
    s = requests.Session()
    ua = UserAgent()
    s.headers={
        'User-Agent': ua.firefox,
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    req =s.get("https://www.vinted."+vintedExtension+"/member/"+username)
    csrfToken=req.text.split('<meta name="csrf-token" content="')[1].split('"')[0]
    s.headers['X-CSRF-Token']=csrfToken
    params = (
        ('localize', 'true'),
    )
    userID=username.split('-')[0]
    response = s.get('https://www.vinted.'+vintedExtension+'/api/v2/users/'+userID, params=params)
    return(response.json()["user"])
