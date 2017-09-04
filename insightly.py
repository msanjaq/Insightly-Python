import time

import requests
from requests.auth import HTTPBasicAuth


class Contacts:
    def __init__(self, auth):
        '''
        Initalizes class
        :param auth: Authorization needed to use Insightly's API
        :type auth: requests.auth.HTTPBasicAuth

        '''
        self.auth = auth
        self.base_url = "https://api.insight.ly/v2.2/Contacts"

    def get(self, cid):
        '''
        Returns the json of a single contact

        :param cid: contact's id
        :type cid: int
        '''
        req = requests.get(self.base_url+"/"+str(cid), auth=self.auth)
        return self._get_json(req)

    def get_all(self):
        '''Returns a list of all the contacts'''
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

            if req.status_code == 200:
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
        '''
        Updates a contact and returns it's json post-update

        :param data: json that will be the result of the update
        :type data: dict
        '''
        req = requests.put(self.base_url, json=data, auth=self.auth)
        return self._get_json(req)

    def create(self, data):
        '''
        Creates a contact and returns it's json post-update

        :param data: json that will be the result of the update
        :type data: dict
        '''
        req = requests.post(self.base_url, json=data, auth=self.auth)
        return self._get_json(req)

    def delete(self, cid):
        '''
        Deletes a contact and returns none.

        :param cid: id of contact that is to be deleted
        :type cid: int
        '''
        req = requests.delete(self.base_url+"/"+str(cid), auth=self.auth)
        self._get_json(req)

    def _get_json(self, req):
        '''
        Raises an error if the request status code is not 200,
        otherwise returns the json object of the request

        :param req: the request that will have its json checked and retuned
        :type req: requests.Requests
        '''
        req.raise_for_status()
        return req.json()


class Insightly:
    def __init__(self, api_key):
        auth = HTTPBasicAuth(api_key, '')
        self.contacts = Contacts(auth)
