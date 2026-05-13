import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "x-api-key": "free_user_3D0LfMOuamW2TIrbcXDxCtHKWT9"
        }

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", headers=self.headers)

    def post(self, endpoint, payload):
        return requests.post(f"{self.base_url}{endpoint}",
                             json=payload,
                             headers=self.headers
                             )
        
        '''
    Older tutorials/videos:

    used ReqRes without auth

    Newer ReqRes:

    often requires API key
    returns 401 otherwise
        '''