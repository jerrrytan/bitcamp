import json
import requests
import urllib

def translate (txt, fr, t):
    args = {
            'client_id': '78c26b15-d1cc-43a7-b24e-fa03c4fb0c81',#your client id here
            'client_secret': 'BRujgswmGMP8zALcygM2GDp0dIf3NHPUifEktis5400',#your azure secret here
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
        }
    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    #oauth_junk = json.loads(requests.post(oauth_url,data=urllib.parse.urlencode(args)).content)
    oauth_response = requests.post(oauth_url,data=args)

    #print(oauth_response)
    oauth_junk = json.loads(oauth_response.text)

    print(t)
    print(fr)
    translation_args = {
            'text': txt,
            'to': t,
            'from': fr,
            }

    headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.parse.urlencode(translation_args),headers=headers)
    return translation_result.text.split('\"')[1]

a=translate ("hello", 'en', 'es')
print (a)
