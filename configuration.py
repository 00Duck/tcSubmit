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
        #gives us directory of THIS script
        self.config_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), "config.json")
    
    def load(self) -> Configuration:
        with open(self.config_dir) as conf:
            configJSON = json.load(conf)
            self.base_path = configJSON["base_path"]
            self.instance_name = configJSON["instance_name"]
            self.shortcuts = configJSON["shortcuts"]
            self.user = configJSON["user"]
            self.password = configJSON["password"]
        return self
    def open(self) -> None:
        os.system(f"code {self.config_dir}")