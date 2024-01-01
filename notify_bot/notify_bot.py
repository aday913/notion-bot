import json
import logging

import requests
from yaml import load, Loader


class NotionBot():
    def __init__(
            self, 
            config_dict : dict, 
            log : logging.Logger,
            ):
        pass

if __name__ == '__main__':
    log = logging.getLogger(__name__)

    with open('config.yaml', 'r') as yml:
        config = load(yml, Loader=Loader)
        print(config)
    
    notionBot = NotionBot()
