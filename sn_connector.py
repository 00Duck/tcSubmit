from configuration import Configuration
import requests
import json

class SNConnector:
    def __init__(self, config: Configuration) -> None:
        self.config = config
        self.session = requests.Session()
        self.endpoint = ''
        self.verb = ''
        self.sn_url = f'https://{self.config.instance_name}.service-now.com'
        self.headers = {'Content-Type': 'application/json'}
        self.params = {}
    
    def test(self):
        try:
            resp = self.session.get(url=f'{self.sn_url}/api/now/table/sys_user?sysparm_query=user_name={self.config.user}&sysparm_fields=user_name,sys_id', headers=self.headers)
            if resp.status_code != 200:
                print(f"Failed connection test to {self.config.instance_name}. Check config.json to ensure the credentials specified are correct.")
                return False
        except Exception as err:
            print(f'Test connection error: {err}')
            return False
        return True
    
    def call(self, inputData: dict) -> requests.Response:
        try:
            resp = ""
            url = f'{self.sn_url}{self.endpoint}'
            data = json.dumps(inputData or {})
            if self.verb in ["POST", "GET", "PUT", "PATCH", "DELETE"]:
                resp = self.session.request(self.verb, url=url, data=data, headers=self.headers, params=self.params)
            else:
                print(f"\nHTTP verb not recognized: {self.verb}")
            return resp
        except Exception as err:
            print(f"\nREST error: {err}")
        return ""