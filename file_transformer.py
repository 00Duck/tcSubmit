from configuration import Configuration
import os
from datetime import datetime, timedelta

class FileTransformer:
    def __init__(self, config: Configuration) -> None:
        self.config = config
        pass

    def process(self, user_input):
        #build path to be base_path/year/1-January/24.md
        print(self.getDatePathFromInput(user_input))

    def getDatePathFromInput(self, input):
        dt = datetime
        match input:
            case None:
                now = dt.now()
                return self.getDatePath(now)
            case "":
                now = dt.now()
                return self.getDatePath(now)
            case "today":
                now = dt.now()
                return self.getDatePath(now)
            case "yesterday":
                now = dt.now() + timedelta(days=-1)
                return self.getDatePath(now)
            case "_":
                return ""
    def getDatePath(self, date: datetime) -> str:
        year = date.strftime("%Y")
        month = date.strftime("%m").lstrip("0") + "-" + date.strftime("%B")
        day = date.strftime("%d").lstrip("0")
        return os.path.join(year, month, day + ".md")