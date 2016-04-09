import json
import requests
import urllib

args = {
        'client_id': '3bcd09ce-2cfb-4857-ab7f-fd9b6b8b25d3',#your client id here
        'client_secret': 'kCygMX9h7Wl3t3TLJExZWXQyJUf+6yJdwWnyZnzqAYI',#your azure secret here
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }
oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
translation_args = {
        'text': "",
        'to': 'zh-CHT',
        'from': 'en'
        }

headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
print translation_result.content