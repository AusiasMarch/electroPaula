import yaml
import requests
import pandas as pd


with open("credentials.yml", 'r') as params:
    credentials = yaml.load(params)


class Ree:
    def __init__(self):
        self.token = credentials['ree_token']


    @staticmethod
    def get_list_archives():
        headers = {'Accept': 'application/json; application/vnd.esios-api-v1+json',
                   'Content-Type': 'application/json',
                   'Host': 'api.esios.ree.es',
                   'Authorization': 'Token token=' + credentials['ree_token'],
                   'Cookie': ''
                   }

        host ='https://api.esios.ree.es'

        r = requests.get(host+'/archives', headers=headers)

        return pd.DataFrame(r.json()['archives'])
