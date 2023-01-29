import getopt, sys
import signal
import json
from configuration import Configuration
from file_transformer import FileTransformer

# Allows for graceful exit when Ctrl + C is pressed during processing
def aborthandler(signum, frame):
    print("\nAborting!", flush=True)
    sys.exit()

def main():
    try:
        conf = Configuration().load()
        ft = FileTransformer(conf)
        ft.process("yesterday")
    except Exception as e:
        print(f'Error loading: {e}')

# def main():
#     arg_list = sys.argv[1:]
#     input_path = ''
#     output_path = ''
#     env = ''
#     range = None

#     signal.signal(signal.SIGINT, aborthandler)

#     try:
#         opts, args = getopt.getopt(arg_list, "ho:i:e:r:", ["output=", "input=", "env=", "range="])
#         for opt, arg in opts:
#             if opt in ("-i", "--input"):
#                 input_path = arg
#             elif opt in ("-o", "--output"):
#                 output_path = arg
#             elif opt in ("-e", "--env"):
#                 env = arg
#             elif opt in ("-r", "--range"):
#                 range = getRanges(arg)
#             elif opt in ("-h", "--help"):
#                 print("""usage: python3 main.py
#     -i, --input   Input xlsx file name.
#     -e, --env     Environment name. Ensure connection.conf is set up properly.
#     -o, --output  Optional. Output xlsx file name. Defaults to output.xlsx.
#     -r, --range   Optional. Range of rows, format <number>:<number>. The first
#                     number is the starting index and the second number is the
#                     number of rows to process.
#                 """)
#                 sys.exit()

#     except getopt.error as err:
#         errExit(str(err))

#     if input_path == "":
#         errExit("Must provide path to excel input")
#     if env == "":
#         errExit("Must provide an instance name")


if __name__ == "__main__":
    main()