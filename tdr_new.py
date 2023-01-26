import os
import sys
import argparse
import pprint
import json
import sys

import zlib

import time

from datetime import date

def __hash(text):
    return '{:x}'.format(zlib.adler32(str.encode(text))).upper()

def __tdr_template(title, file, line, column):
    tpl = {
        "id": "TDR_" + __hash(title + str(time.time())),
        "brief": title,
        "author": os.getlogin(),
        "date": date.today().strftime("%Y-%m-%d"),
        "description": "",
        "owner": "",
        "category": "techdebt",
        "severity": "warning",
        "priority": "",
        "file": file,
        "line": line,
        "column": column,
        "votes": 1,
        "discussion": [],
        "tags": []
    }
    return tpl


def tdr_new(dir, title, file, line, column):
    if type(title) == list:
        title_dashed = "-".join(title).replace(' ', '-')
        title_spaced = " ".join(title)
    elif type(title) == str:
        title_dashed = (title).replace(' ', '-')
        title_spaced = title

    tdrFilePath = os.path.join(os.path.abspath(
        dir), ".tdr", title_dashed+".tdr")

    # Create directories
    os.makedirs(os.path.dirname(tdrFilePath), exist_ok=True)

    # Create TDR file if not exist
    if not os.path.exists(tdrFilePath):
        with open(os.path.abspath(tdrFilePath), "w") as jsonFile:
            tpl = __tdr_template(title_spaced, file, line, column)
            jsonObj = json.dumps(tpl, indent=4)
            jsonFile.write(jsonObj)
            print("[TDR] Created TDR: " + tdrFilePath)
    else:
        print("[TDR] TDR already present: " + tdrFilePath)


def main():
    parser = argparse.ArgumentParser(
        prog='tdr_new',
        description='Technical Debt Record Tool - Create new technical debt')
    parser.add_argument('title', metavar='Title of TDR',
                        nargs='+', help='Title of the TDR')
    parser.add_argument("--path", "-p", help="Path", type=str, default=".")
    parser.add_argument("--file", "-f", help="File/Folder in debt (relative)", type=str, default=".")
    parser.add_argument("--line", "-l", help="Line in debt", type=int, default=0)
    parser.add_argument("--column", "-c", help="Column in debt", type=int, default=0)

    args = parser.parse_args()

    tdr_new(args.path, args.title, args.file, args.line, args.column)

    return 0


if __name__ == '__main__':
    sys.exit(main())
