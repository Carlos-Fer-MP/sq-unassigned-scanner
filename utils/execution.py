import getopt
import os
import sys
from time import strftime, gmtime


def parse_flag_arguments(argv):
    environment = login = password = token = ''

    try:
        opts, _args = getopt.getopt(argv, "he:l:p:t:u:c:d:")
    except getopt.GetoptError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

    for opt, arg in opts:
        if opt in "-e":
            environment = arg
        elif opt in "-l":
            login = arg
        elif opt in "-p":
            password = arg
        elif opt in "-t":
            token = arg

    return {
        "environment": environment,
        "login": login,
        "password": password,
        "token": token
    }


class Logger(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()


def execution_logging(environment):
    log_directory = "logs/" + str(environment)

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = open(log_directory + "/log" + strftime("_%d_%b_%Y_%H-%M-%S", gmtime()) + '.txt', 'w')

    sys.stdout = Logger(sys.stdout, log_file)
