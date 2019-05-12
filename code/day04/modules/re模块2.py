
# -*- coding: UTF-8 -*-
import json
import requests
import re

def get_by_request():
    username = 'insta360official'
    url = 'https://www.instagram.com/' + username + '/'
    response = requests.get(url=url, verify=False)
    page = response.text
    pattern = re.compile("window._sharedData = (.*?);</script>", re.S)
    items = re.findall(pattern, page)
    jsonData = json.loads(items[0])
    count = jsonData['entry_data']['ProfilePage'][0]['user']['followed_by']['count']
    return count

if __name__ == "__main__":
    get_by_request()
