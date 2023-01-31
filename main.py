import getopt, sys
import signal
from submit import Submit
from configuration import Configuration

# Allows for graceful exit when Ctrl + C is pressed during processing
def aborthandler(signum, frame):
    print("\nAborting!", flush=True)
    sys.exit()

# Convenience function for exiting when there's a problem
def errExit(msg: str) -> None:
    print(msg)
    sys.exit()

def main():
    arg_list = sys.argv[1:]
    user_input = ''
    signal.signal(signal.SIGINT, aborthandler)

    try:
        opts, args = getopt.getopt(arg_list, "hd:c", ["date=", "config="])
        for opt, arg in opts:
            if opt in ("-d", "--date"):
                user_input = arg
            elif opt in ("-c", "--config"):
                try:
                    Configuration().open()
                except Exception as e:
                    print(f"{e}")
                finally:
                    sys.exit()
            elif opt in ("-h", "--help"):
                print("""usage: submit -d today|yesterday|YYYY-MM-DD|YYYY/MM/DD
    -d, --date      Date to submit hours for. Enter today, yesterday, YYYY-MM-DD, or YYYY/MM/DD.
    -c, --config    Opens the config.json file using VSCode. Must have VSCode installed to use.
    -h, --help      Displays this help message
                """)
                sys.exit()

    except getopt.error as err:
        errExit(str(err))

    if user_input == "":
        errExit("Must provide a date to submit hours.")
    
    Submit().execute(user_input)

if __name__ == "__main__":
    main()