import time

import requests
from requests.auth import HTTPBasicAuth


class Entity:
    def __init__(self, auth, base_url):
        '''
        Initalizes class

        :param auth: Authorization needed to use Insightly's API
        :type auth: requests.auth.HTTPBasicAuth
        :param base_url: the api url base component
        :type url: str
        '''
        self.auth = auth
        self.base_url = base_url

    def get(self, eid):
        '''
        Gets the json of a single entity

        :param eid: Id of the entity
        :type eid: int
        '''
        req = requests.get(self.base_url+"/"+str(eid), auth=self.auth)
        return self._get_json(req)

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

    def _get_json(self, req):
        '''
        Raises an error if the request status code is not 200,
        otherwise returns the json object of the request

        :param req: the request that will have its json checked and retuned
        :type req: requests.Requests
        '''
        req.raise_for_status()
        return req.json()


class Contacts(Entity):
    def __init__(self, auth):
        '''
        Initalizes class

        :param auth: Authorization needed to use Insightly's API
        :type auth: requests.auth.HTTPBasicAuth
        '''
        Entity.__init__(self, auth, "https://api.insight.ly/v2.2/Contacts")

    def get_all(self, brief=False):
        '''
        Returns a list of all the contacts

        :param brief: Whether the API strips the contact's child objects
        '''
        result = []

        params = {"brief": brief, "skip": 0, "top": 500, "count_total": True}
        req = requests.get(self.base_url, auth=self.auth, params=params)
        count = int(req.headers["X-Total-Count"])

        while count >= 0:
            req = requests.get(self.base_url, auth=self.auth, params=params)

            if req.status_code == 200:
                pass

            elif req.status_code == 429:
                time.sleep(1)
                req = requests.get(self.base_url, auth=self.auth)

            else:
                req.raise_for_status()

            result += req.json()
            count -= params["top"]
            params["skip"] += params["top"]

        return result

    def delete(self, cid):
        '''
        Deletes a contact and returns none.

        :param cid: id of contact that is to be deleted
        :type cid: int
        '''
        req = requests.delete(self.base_url+"/"+str(cid), auth=self.auth)
        req.raise_for_status()


class Organisations(Entity):
    def __init__(self, auth):
        Entity.__init__(self, auth,
                        "https://api.insight.ly/v2.2/Organisations")


class Insightly:
    def __init__(self, api_key):
        auth = HTTPBasicAuth(api_key, '')
        self.contacts = Contacts(auth)
        self.organisations = Organisations(auth)
