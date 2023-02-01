from configuration import Configuration
from file_transformer import FileTransformer
from file_sender import FileSender
import sys

class Submit:
    def __init__(self) -> None:
        pass
    def execute(self, user_input):
        try:
            conf = Configuration().load()
            ft = FileTransformer(conf).process(user_input)
            if len(ft.timelogs) == 0:
                print("No time logs for today to submit")
                sys.exit()
            FileSender(conf).upsert(ft.timelogs)
        except Exception as e:
            print(f'{e}')