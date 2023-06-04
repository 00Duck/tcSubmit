from sn_connector import SNConnector
from configuration import Configuration
import json

class FileSender:
    def __init__(self, config: Configuration) -> None:
        self.config = config

    def upsert(self, timelogs):
        snc = SNConnector(self.config)
        snc.session.auth = (self.config.user, self.config.password)
        if not snc.test():
            return False
        update_count = 0
        create_count = 0
        for timelog in timelogs:
            log_sys_id = self.getExistingLog(snc, timelog)
            if log_sys_id != None:
                res = self.updateUpsert(snc, timelog.__dict__, log_sys_id)
                if res:
                    update_count += 1
            else:
               res = self.createUpsert(snc, timelog.__dict__)
               if res:
                    create_count += 1
        print(f"Logs created: {create_count}, updated: {update_count}")
        return True