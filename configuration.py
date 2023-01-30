from __future__ import annotations
import json
import os

class Configuration:
    def __init__(self) -> None:
        self.base_path = ""
        self.instance_name = ""
        self.shortcuts = []
        self.user = ""
        self.password = ""
    
    def load(self) -> Configuration:
        #gives us directory of this script
        file_dir = os.path.realpath(os.path.dirname(__file__))
        config_dir = os.path.join(file_dir, "config.json")
        with open(config_dir) as conf:
            configJSON = json.load(conf)
            self.base_path = configJSON["base_path"]
            self.instance_name = configJSON["instance_name"]
            self.shortcuts = configJSON["shortcuts"]
            self.user = configJSON["user"]
            self.password = configJSON["password"]
        return self
