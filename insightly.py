import json
import time

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint


class Contacts:
    def __init__(self, auth):
        self.auth = auth
        self.base_url = "https://api.insight.ly/v2.2/Contacts"

    def get(self, cid):
        return requests.get(self.base_url+"/"+str(cid), auth=self.auth).json()

    def get_all(self):
        count_url = self.base_url + "?brief=false&top=1&count_total=true"
        count = int(requests.get(count_url,
                                 auth=self.auth).headers["X-Total-Count"])

        result = []
        skip = 0
        top = 5

        while count >= 0:
            url = "{}?brief=false&skip={}&top={}".format(self.base_url,
                                                         skip,
                                                         top)
            req = requests.get(url, auth=self.auth)

            if req.status_code == 429:
                time.sleep(1)
                req = requests.get(url, auth=self.auth)

            result += req.json()
            count -= top
            skip += top

        return result

    def update(self, data):
        req = requests.put(self.base_url, json=data, auth=self.auth)

        if req.status_code == 429:
            time.sleep(1)
            req = requests.put(self.base_url, json=data, auth=self.auth)

        return req.json()


class Insightly:
    def __init__(self, api_key):
        auth = HTTPBasicAuth(api_key, '')
        self.contacts = Contacts(auth)
