from datetime import datetime
from configuration import Configuration
from file_transformer import FileTransformer
import time, signal, sys, os
from submit import Submit

class AutoRun:
    def __init__(self) -> None:
        self.conf = Configuration().load()
        self.ft = FileTransformer(self.conf)
        self.cached_stamp = 0

    def aborthandler(self, signum, frame):
        print(f"\nExited - {signum}", flush=True)
        sys.exit()

    def start(self):
        signal.signal(signal.SIGINT, self.aborthandler)
        while (True):
            path = os.path.join(self.conf.base_path, self.ft.getDatePath(datetime.now()))
            if not os.path.exists(path):
                continue
            if self.cached_stamp == 0:
                self.cached_stamp = os.stat(path).st_mtime
                continue
            current_stamp = os.stat(path).st_mtime
            if current_stamp != self.cached_stamp:
                Submit().execute("today")
                self.cached_stamp = current_stamp
            time.sleep(5)

def main():
    try:
        AutoRun().start()
    except Exception as e:
        print(f"{e}")
        sys.exit()

if __name__ == "__main__":
    main()