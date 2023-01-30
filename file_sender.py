from sn_connector import SNConnector
from timelog import TimeLog
from configuration import Configuration
import json

class FileSender:
    def __init__(self, config: Configuration) -> None:
        self.config = config

    def upsert(self, timelogs):
        snc = SNConnector(self.config)
        snc.endpoint = "/api/now/table/x_teth_isc_time_log"
        snc.session.auth = (self.config.user, self.config.password)
        if not snc.test():
            return False
        update_count = 0
        create_count = 0
        for timelog in timelogs:
            log_sys_id =  self.getExistingLog(snc, timelog)
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

    #The create portion of the upsert function
    def createUpsert(self, snc: SNConnector, timelog: TimeLog):
        snc.verb = "POST"
        snc.endpoint = "/api/now/table/x_teth_isc_time_log"
        resp = snc.call(timelog)
        if resp.status_code != 201:
            print("Error creating on upsert: " + resp.text)
            return False
        return True

    #The update portion of the upsert function
    def updateUpsert(self, snc: SNConnector, timelog: TimeLog, log_sys_id: str):
        snc.verb = "PATCH"
        snc.endpoint = f"/api/now/table/x_teth_isc_time_log/{log_sys_id}"
        resp = snc.call(timelog)
        if resp.status_code != 200:
            print("Error updating on upsert: " + resp.text)
            return False
        return True

    #The get portion of the upsert function (check for existing log)
    def getExistingLog(self, snc: SNConnector, timelog: TimeLog):
        snc.verb = "GET"
        ld = f"{timelog.log_date}@javascript:gs.dateGenerate('{timelog.log_date}','start')@javascript:gs.dateGenerate('{timelog.log_date}','end')"
        snc.session.params = {
            "sysparm_query": f"resource.user_name={timelog.resource}^project={timelog.project}^log_dateON{ld}",
            "sysparm_fields": "sys_id"
        }
        
        resp = snc.call({})
        snc.session.params = {} #reset here to make sure we don't use elsewhere
        if resp.status_code != 200:
            return None
        try:
            respJSON = json.loads(resp.text)
            if len(respJSON["result"]) == 1:
                return respJSON["result"][0]["sys_id"]
        except:
            return None
        return None
