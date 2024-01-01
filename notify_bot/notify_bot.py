import json
import logging

import requests
from yaml import load, Loader


class NotionBot():
    def __init__(
            self, 
            config_dict : dict
            ):
        self.log = logging.getLogger(__name__)
        self.API_KEY, self.databases = self.set_configuration_options(config_dict=config_dict)

        self.url = 'https://api.notion.com/v1/databases'
        self.headers = {
            'Authorization' : f'{self.API_KEY}',
            'Notion-Version' : '2022-06-28',
            'Content-Type' : 'application/json'
        }
        
    def reset_config_options(self, config_file : dict):
        config_dict = self.read_config_yaml_file(config_file)
        self.API_KEY, self.databases = self.set_configuration_options(config_dict=config_dict)
        return
    
    def set_configuration_options(self, config_dict : dict):
        api_key = config_dict['api_key']
        self.log.info(f'Using api key {api_key}')
        databases = {}
        for db in config_dict['databases']:
            label = list(db.keys())[0]
            databases[label] = db[label]
        self.log.info(f'Database configurations: {databases}')
        return api_key, databases
        
    def read_config_yaml_file(self, config_file : str) -> dict:
        config = None
        with open(config_file, 'r') as yml:
            config = load(yml, Loader=Loader)
        if config:
            return config
        else:
            raise FileNotFoundError(f"Could not load configuration yaml file {config_file}")
        
    def query_db(self, db_label : str, filter_json : dict):
        pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    with open('config.yaml', 'r') as yml:
        config = load(yml, Loader=Loader)
        # print(config)
    
    notionBot = NotionBot(config)
