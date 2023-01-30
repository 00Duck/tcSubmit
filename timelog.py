class TimeLog:
    def __init__(self) -> None:
        self.project = ""
        self.work_hours = 0.0
        self.notes = ""
        self.log_date = ""
        self.resource = ""
    def __str__(self) -> str:
        return self.project + " " + str(self.work_hours) + " " + self.log_date + " " + self.resource + " " + self.notes
