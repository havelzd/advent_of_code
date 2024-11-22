import sys
import shutil
import os
import argparse

VERSION = "0.1.0"
SESSION_COOKIE = "session.txt"

CWD = os.getcwd()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_NAME = ".aoc_config"
CONFIG_FILE = os.path.join(BASE_DIR, CONFIG_NAME)

USAGE_INFO = "Script to automate certain AOC tasks - init / submit"

parser = argparse.ArgumentParser(
    description=USAGE_INFO)
subparsers = parser.add_subparsers(dest="command", help="Commands")

config_parser = subparsers.add_parser("config", help="Setup sessid cookie")
config_parser.add_argument(
    "opt", choices=['sessid'], help="config key")
config_parser.add_argument(
    "value", help="config value")

init_parser = subparsers.add_parser("init", help="Initialize solution")
init_parser.add_argument(
    "-d", nargs="+", metavar=('day', 'year'), required=False, help="Day, year of solution")
init_parser.add_argument("-t", "--template", required=False,
                         help="Path to template")
init_parser.add_argument(
    "-i", "--input", required=False, help="The directory to save the input (relative to year/day dir)")


submit_parser = subparsers.add_parser("submit", help="Submit solution")
submit_parser.add_argument(
    "year", type=int, help="The year of the advent of code")
submit_parser.add_argument(
    "day", type=int, help="The day of the advent of code")
submit_parser.add_argument("level", type=int, help="The level of the solution")
submit_parser.add_argument(
    "-s", required=False, help="The value of the solution")


def __submit_solution(year, day, level, value, session):
    # submit aoc solution for given year / day
    # curl -X POST -H 'Cookie: session=<session>' -d "level=1&answer=<value>" https://adventofcode.com/2020/day/1/answer
    year_full = year if year >= 2000 else year + 2000
    curl_cmd = f"curl -X POST -H 'Cookie: session={session}' " + \
        f"-d 'level={level}&answer={value}' " + \
        f"https://adventofcode.com/{year_full}/day/{day}/answer"
    return os.system(curl_cmd)


def __fetch_input(year, day, session, input_dir):
    year_full = year if year >= 2000 else year + 2000
    curl_cmd = f"curl -H 'Cookie: session={session}' " + \
        f"https://adventofcode.com/{year_full}/day/{day}/input" + \
        f" > {year}/{day}/{input_dir}/input.txt"
    return os.system(curl_cmd)


if __name__ == "__main__":
    print(__file__)
    parsed_args = parser.parse_args()
    print(parsed_args)

    if parsed_args.command == 'config':
        opt, value = parsed_args.opt, parsed_args.value
        print(f"setting <{opt}> to \"{value}\"")
        with open(CONFIG_FILE, "w") as f:
            f.write(f"{opt}={value}")
        pass

    elif parsed_args.command == 'init':
        dir = parsed_args.d
        print(f"Initializing solution dir for {dir}")
        if len(dir) == 2:
            # create directory for the solution for cwd
            year, day = dir
        input = parsed_args.input
    else:
        print("No arguments provided. Run with -h for help.")
        sys.exit(1)

        # year, day = parsed_args.year, parsed_args.day
        # template_dir = parsed_args.template
        # input_dir = parsed_args.input
        # submit = parsed_args.submit
        # cookie = parsed_args.cookie
        #
        # os.makedirs(f"{year}/{day}", exist_ok=True)
        #
        # SSID = None
        # ssid_file = SESSION_COOKIE
        # if input_dir or submit:
        #     if cookie:
        #         if os.path.exists(cookie) and os.path.isfile(cookie):
        #             ssid_file = cookie
        #         else:
        #             SSID = cookie
        #     if SSID is None and os.path.exists(ssid_file):
        #         with open(ssid_file) as f:
        #             SSID = f.read().strip()
        #     print(f"Session cookie: {SSID}\n")
        #
        # # copy template content to the year/day directory
        # if template_dir and os.path.exists(template_dir):
        #     if os.path.isdir(template_dir):
        #         shutil.copytree(template_dir, f"{year}/{day}", dirs_exist_ok=True)
        #     elif os.path.isfile(template_dir):
        #         # execute the file inside the year/day directory
        #         print("Not supported yet.")
        #         sys.exit(3)
        #
        # # fetch input into provided directory
        # if input_dir:
        #     os.makedirs(f"{year}/{day}/{input_dir}", exist_ok=True)
        #     __fetch_input(year, day, SSID, input_dir)
        #
        # if submit:
        #     __submit_solution(year, day, *submit, SSID)
