from configuration import Configuration
import os, re
from datetime import datetime, timedelta
from timelog import TimeLog

class FileTransformer:
    def __init__(self, config: Configuration) -> None:
        self.config = config
        self.timelogs = []
        pass

    def process(self, user_input):
        #build path to be base_path/year/1-January/24.md
        path = os.path.join(self.config.base_path, self.getDatePathFromInput(user_input))
        with open(path) as f:
            note_collect_mode = False
            timelog = TimeLog()
            for line in f:
                project_id = self.getProject(line)
                if project_id != None:
                    note_collect_mode = True
                    timelog.project = project_id
                    timelog.work_hours = self.getHours(line)
                    timelog.log_date = self.getLogDate(user_input)
                    timelog.resource = self.config.user
                    continue
                if note_collect_mode and line != "\n":
                    timelog.notes += line
                if note_collect_mode and line == "\n": #End of note, process and start over
                    note_collect_mode = False
                    self.timelogs.append(timelog)
                    timelog = TimeLog()
            #file read ended while we were in note mode, send what we have
            if note_collect_mode:
                self.timelogs.append(timelog)
        return self

    #Returns log date in the same way the date path was parsed (based on input)
    def getLogDate(self, input):
        dt = datetime
        match input:
            case None:
                return dt.now().date().isoformat()
            case "":
                return dt.now().date().isoformat()
            case "today":
                return dt.now().date().isoformat()
            case "yesterday":
                now = dt.now() + timedelta(days=-1)
                return now.date().isoformat()
            case _:
                now = self.getDateFromStr(input)
                return now.date().isoformat()

    #Returns the portion of the path /2023/1-January/24.md
    # Can input date in format YYYY-MM-DD, YYYY/MM/DD, yesterday, or today
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
            case _:
                now = self.getDateFromStr(input)
                return self.getDatePath(now)

    #Returns actual date portion string
    def getDatePath(self, date: datetime) -> str:
        year = date.strftime("%Y")
        month = date.strftime("%m").lstrip("0") + "-" + date.strftime("%B")
        day = date.strftime("%d").lstrip("0")
        return os.path.join(year, month, day + ".md")

    #Takes format YYYY-MM-DD or YYYY/MM/DD string and returns a date
    def getDateFromStr(self, date_str: str) -> datetime:
        date_arr = re.split('\\\\|-', date_str)
        return datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))

    def getProject(self, line: str) -> str:
        for (k, v) in self.config.shortcuts.items():
            if line.startswith(k):
                return v
        return None

    def getHours(self, line: str) -> float:
        hours_list = re.split(" ", line)
        if len(hours_list) != 2:
            return float(0.0)
        if hours_list[1] == "" or hours_list[1] == None or hours_list[1] == '\n':
            return float(0.0)
        return float(hours_list[1])