from __future__ import annotations
import json
import os
from dotenv import load_dotenv

class Configuration:
    def __init__(self) -> None:
        self.base_path = ""
        self.instance_name = ""
        self.shortcuts = []
        self.user = ""
        self.password = ""
        #gives us directory of THIS script
        self.local_dir = os.path.realpath(os.path.dirname(__file__))
        self.config_path = os.path.join(self.local_dir, "config.json")
        self.env_path = os.path.join(self.local_dir, ".env")
    
    def load(self) -> Configuration:
        load_dotenv(self.env_path)
        with open(self.config_path) as conf:
            config_json = json.load(conf)
            self.shortcuts = config_json["shortcuts"]
            self.base_path = os.environ.get("BASE_PATH")
            self.instance_name = os.environ.get("INSTANCE_NAME")
            self.user = os.environ.get("SN_USER")
            self.password = os.environ.get("SN_PASS")
        return self
    def open(self) -> None:
        os.system(f"code {self.config_path}")