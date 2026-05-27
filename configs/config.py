import logging
from typing import Dict

class Config:
    def __init__(self, config_dict: Dict):
        self.config_dict = config_dict

    def get_config(self, key: str):
        try:
            return self.config_dict[key]
        except KeyError:
            logging.error(f'Config key {key} not found')
            raise ValueError(f'Config key {key} not found')

    def set_config(self, key: str, value: str):
        self.config_dict[key] = value

# Create a config instance
config = Config({"db_url": "localhost:5432", "db_user": "user", "db_password": "password"})