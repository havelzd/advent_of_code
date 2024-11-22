import sys
import shutil
import os
import argparse

VERSION = "0.1.0"
SESSION_COOKIE = "session.txt"


parser = argparse.ArgumentParser(
    description="Initialize advent of code project. Create directory for /year/day, possibly copy given template, fetch input and submit solutions.")
parser.add_argument(
    "year", type=int, help="The year of the advent of code")
parser.add_argument("day", type=int, help="The day of the advent of code")
parser.add_argument("-t", "--template", required=False,
                    help="Path to template")
parser.add_argument(
    "-i", "--input", required=False, help="The directory to save the input (relative to year/day dir)")
parser.add_argument(
    "-s", "--submit", required=False, nargs="+",  metavar=("level", "solution"), help="Submit first or second solution")
parser.add_argument("-c", "--cookie", required=False,
                    help="cookie or path to file containing cookie. Defaults to session.txt in the current directory")


def __process_args():

    # Check if there's piped input
    if not sys.stdin.isatty():  # This checks if input comes from a pipe
        piped_input = sys.stdin.read().strip()
    else:
        piped_input = None

    parsed_args = parser.parse_args()

    if parsed_args.submit:
        if piped_input:
            parsed_args.submit.append(piped_input)
        else:
            print("Solution value is required to submit.")
            sys.exit(6)

    print(parsed_args)
    return parsed_args


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
    parsed_args = __process_args()
    year, day = parsed_args.year, parsed_args.day
    template_dir = parsed_args.template
    input_dir = parsed_args.input
    submit = parsed_args.submit
    cookie = parsed_args.cookie

    os.makedirs(f"{year}/{day}", exist_ok=True)

    SSID = None
    ssid_file = SESSION_COOKIE
    if input_dir or submit:
        if cookie:
            if os.path.exists(cookie) and os.path.isfile(cookie):
                ssid_file = cookie
            else:
                SSID = cookie
        if SSID is None and os.path.exists(ssid_file):
            with open(ssid_file) as f:
                SSID = f.read().strip()
        print(f"Session cookie: {SSID}\n")

    # copy template content to the year/day directory
    if template_dir and os.path.exists(template_dir):
        if os.path.isdir(template_dir):
            shutil.copytree(template_dir, f"{year}/{day}", dirs_exist_ok=True)
        elif os.path.isfile(template_dir):
            # execute the file inside the year/day directory
            print("Not supported yet.")
            sys.exit(3)

    # fetch input into provided directory
    if input_dir:
        os.makedirs(f"{year}/{day}/{input_dir}", exist_ok=True)
        __fetch_input(year, day, SSID, input_dir)

    if submit:
        __submit_solution(year, day, *submit, SSID)
