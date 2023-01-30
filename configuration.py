from __future__ import annotations
import json
import sys

class Configuration:
    def __init__(self) -> None:
        self.base_path = ""
        self.instance_name = ""
        self.shortcuts = []
        self.user = ""
        self.password = ""
    
    def load(self) -> Configuration:
        with open("config.json") as conf:
            configJSON = json.load(conf)
            self.base_path = configJSON["base_path"]
            self.instance_name = configJSON["instance_name"]
            self.shortcuts = configJSON["shortcuts"]
            self.user = configJSON["user"]
            self.password = configJSON["password"]
        return self