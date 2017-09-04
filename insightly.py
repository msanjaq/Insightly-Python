import time

import requests
from requests.auth import HTTPBasicAuth


class Contacts:
    def __init__(self, auth):
        self.auth = auth
        self.base_url = "https://api.insight.ly/v2.2/Contacts"

    def get(self, cid):
        req = requests.get(self.base_url+"/"+str(cid), auth=self.auth)
        req.raise_for_status()
        return req.json()

    def get_all(self):
        count_url = self.base_url + "?brief=false&top=1&count_total=true"
        count = int(requests.get(count_url,
                                 auth=self.auth).headers["X-Total-Count"])

        result = []
        skip = 0
        top = 500

        while count >= 0:
            url = "{}?brief=false&skip={}&top={}".format(self.base_url,
                                                         skip,
                                                         top)
            req = requests.get(url, auth=self.auth)

            if req.status_code == 400:
                pass

            elif req.status_code == 429:
                time.sleep(1)
                req = requests.get(url, auth=self.auth)

            else:
                req.raise_for_status()

            result += req.json()
            count -= top
            skip += top

        return result

    def update(self, data):
        req = requests.put(self.base_url, json=data, auth=self.auth)
        req.raise_for_status()
        return req.json()

    def create(self, data):
        req = requests.post(self.base_url, json=data, auth=self.auth)


class Insightly:
    def __init__(self, api_key):
        auth = HTTPBasicAuth(api_key, '')
        self.contacts = Contacts(auth)
