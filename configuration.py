from __future__ import annotations
import json
import sys

class Configuration:
    def __init__(self) -> None:
        self.base_path = ''
        self.instance_name = ''
        self.shortcuts = []
    
    def load(self) -> Configuration:
        with open("config.json") as conf:
            configJSON = json.load(conf)
            self.base_path = configJSON["base_path"]
            self.instance_name = configJSON["instance_name"]
            self.shortcuts = configJSON["shortcuts"]
        return self
